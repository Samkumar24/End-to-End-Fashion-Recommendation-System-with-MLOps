from src.recommendation_system.constants import CONFIG_PATH
from src.recommendation_system.utils.common import read_yaml , create_dir
from dataclasses import dataclass
from src.recommendation_system.logging import logger
import pickle
import os
import pandas as pd
import mlflow
from src.recommendation_system.entity import model_evalulation_config
import numpy as np


class model_evalulation_congif:

    def __init__(self, config):
        self.config     = config
        self.sim_matrix = None
        self.df         = None

    def load_artifacts(self):
        try:
            logger.info("=" * 20 + " Loading Artifacts STARTED " + "=" * 20)
            with open(self.config.sim_matrix_path, 'rb') as f:
                self.sim_matrix = pickle.load(f)
            with open(self.config.featured_df_path, 'rb') as f:
                self.df = pickle.load(f)
            logger.info("sim_matrix : %s", str(self.sim_matrix.shape))
            logger.info("df         : %s", str(self.df.shape))
            logger.info("=" * 20 + " Loading Artifacts COMPLETED " + "=" * 20)

        except Exception as e:
            logger.error("Load artifacts FAILED - %s", str(e))
            raise e

    def get_test_sample(self) -> pd.DataFrame:
        try:
            logger.info("=" * 20 + " Test Sample STARTED " + "=" * 20)

            # 5 products per aesthetic — balanced test set
            test_set = (
                self.df.groupby("aesthetic", group_keys=False)
                       .apply(lambda x: x.sample(min(5, len(x)), random_state=42))
                       .drop_duplicates()
                       .reset_index(drop=True)
            )

            logger.info("Sample size : %d", len(test_set))
            logger.info("=" * 20 + " Test Sample COMPLETED " + "=" * 20)
            return test_set

        except Exception as e:
            logger.error("Test sample FAILED - %s", str(e))
            raise e

    # ── ground truth — similarity threshold ──────────
    def get_relevant(self, product_id, threshold=0.4):
        scores = self.sim_matrix[product_id].copy()
        return [
            i for i, s in enumerate(scores)
            if s >= threshold and i != product_id
        ]

    # ── precision@k ──────────────────────────────────
    def precision_at_k(self, top_idx, relevant_idx, k) -> float:
        hits = len(set(top_idx[:k]) & set(relevant_idx))
        return hits / k if k > 0 else 0.0

    # ── ndcg@k ───────────────────────────────────────
    def ndcg_at_k(self, top_idx, relevant_idx, k) -> float:
        relevant_set = set(relevant_idx)
        dcg  = sum(
            1 / np.log2(i + 2)
            for i, idx in enumerate(top_idx[:k])
            if idx in relevant_set
        )
        idcg = sum(1 / np.log2(i + 2) for i in range(min(k, len(relevant_set))))
        return dcg / idcg if idcg > 0 else 0.0

    # ── map ──────────────────────────────────────────
    def map_score(self, top_idx, relevant_idx, k) -> float:
        relevant_set = set(relevant_idx)
        hits, score  = 0, 0.0
        for i, idx in enumerate(top_idx[:k]):
            if idx in relevant_set:
                hits  += 1
                score += hits / (i + 1)
        return score / len(relevant_set) if relevant_set else 0.0

    def score_product(self, row, top_k=10, threshold=0.5) -> dict:
        try:
            product_id   = row.name
            relevant_idx = self.get_relevant(product_id, threshold)

            scores             = self.sim_matrix[product_id].copy()
            scores[product_id] = -1
            top_idx            = scores.argsort()[::-1][0:top_k]

            precision = self.precision_at_k(top_idx, relevant_idx, top_k)
            ndcg      = self.ndcg_at_k(top_idx,      relevant_idx, top_k)
            map_s     = self.map_score(top_idx,       relevant_idx, top_k)

            logger.info(
                "%-35s | P@K=%.2f | NDCG=%.2f | MAP=%.2f",
                row["product_name_clean"][:35],
                precision, ndcg, map_s
            )

            return {
                "product_name_clean" : row["product_name_clean"],
                "aesthetic"          : row["aesthetic"],
                "n_relevant"         : len(relevant_idx),
                "precision_at_k"     : round(precision, 4),
                "ndcg_at_k"          : round(ndcg,      4),
                "map"                : round(map_s,     4),
            }

        except Exception as e:
            logger.error("score_product FAILED - %s", str(e))
            raise e

    def run_evaluation(self, top_k=10, threshold=0.4):
        try:
            logger.info("=" * 20 + " Evaluation STARTED " + "=" * 20)

            if self.df is None or self.sim_matrix is None:
                self.load_artifacts()

            test_sample = self.get_test_sample()
            logger.info("Scoring %d products", len(test_sample))

            records = []
            for _, row in test_sample.iterrows():
                result = self.score_product(row, top_k=top_k, threshold=threshold)
                records.append(result)

            metrics_df = pd.DataFrame(records)

            summary = {
                "n_products_tested" : len(metrics_df),
                "top_k"             : top_k,
                "threshold"         : threshold,
                "precision_at_k"    : round(metrics_df["precision_at_k"].mean(), 4),
                "ndcg_at_k"         : round(metrics_df["ndcg_at_k"].mean(),      4),
                "map"               : round(metrics_df["map"].mean(),             4),
            }

            # save csv
            out_path = os.path.join(
                self.config.model_eval_metrics, 'eval_metrics.csv'
            )
            metrics_df.to_csv(out_path, index=False)

            # ── MLflow ───────────────────────────────────
            mlflow.set_tracking_uri(self.config.ml_flow_tracking_uri)
            mlflow.set_experiment(self.config.ml_flow_experiment_name)

            with mlflow.start_run(run_name=self.config.ml_flow_run_name) as run:

                mlflow.log_param("top_k",     top_k)
                mlflow.log_param("threshold", threshold)
                mlflow.log_param("n_tested",  len(metrics_df))

                mlflow.log_metric("precision_at_k", summary["precision_at_k"])
                mlflow.log_metric("ndcg_at_k",      summary["ndcg_at_k"])
                mlflow.log_metric("map",             summary["map"])

                mlflow.log_artifact(out_path)

                run_id        = run.info.run_id
                experiment_id = run.info.experiment_id
                run_url       = f"{self.config.ml_flow_tracking_uri}/#/experiments/{experiment_id}/runs/{run_id}"

            # ── log summary ──────────────────────────────
            logger.info("======= SUMMARY =======")
            for k, v in summary.items():
                logger.info("%-25s : %s", k, v)
            logger.info("Run ID  : %s", run_id)
            logger.info("Run URL : %s", run_url)
            logger.info("=" * 20 + " Evaluation COMPLETED " + "=" * 20)

            # ── return AFTER mlflow ───────────────────────
            return summary, metrics_df, run_id, run_url

        except Exception as e:
            logger.error("Evaluation FAILED - %s", str(e))
            raise e
