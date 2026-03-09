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
from datetime import datetime

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

        # ── Save timestamped CSV ──────────────────────
        timestamp = datetime.now().strftime("%Y_%m_%d")
        out_path  = os.path.join(
            self.config.model_eval_metrics,
            f'eval_{timestamp}_metrics.csv'
        )
        metrics_df.to_csv(out_path, index=False)
        logger.info("Metrics saved: %s", out_path)

        # ── MLflow + DagsHub ──────────────────────────
        from dotenv import load_dotenv
        from pathlib import Path
        load_dotenv(dotenv_path=Path("C:/Users/sam/End-to-End-Fashion-Recommendation-System-with-MLOps/.env"), override=True)

        os.environ["MLFLOW_TRACKING_USERNAME"] = os.getenv("MLFLOW_TRACKING_USERNAME")
        os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv("MLFLOW_TRACKING_PASSWORD")

        mlflow.set_tracking_uri(self.config.ml_flow_tracking_uri)
        mlflow.set_experiment(self.config.ml_flow_experiment_name)

        with mlflow.start_run(run_name=self.config.ml_flow_run_name) as run:
            mlflow.log_param("top_k",     top_k)
            mlflow.log_param("threshold", threshold)
            mlflow.log_param("n_tested",  len(metrics_df))

            mlflow.log_metric("precision_at_k", summary["precision_at_k"])
            mlflow.log_metric("ndcg_at_k",      summary["ndcg_at_k"])
            mlflow.log_metric("map",            summary["map"])

            

            run_id        = run.info.run_id
            experiment_id = run.info.experiment_id

        # ── DagsHub URL ───────────────────────────────
        run_url = f"https://dagshub.com/samkumarr24/End-to-End-Fashion-Recommendation-System-with-MLOps/experiments/{experiment_id}/runs/{run_id}"

        # ── log summary ───────────────────────────────
        logger.info("======= SUMMARY =======")
        for k, v in summary.items():
            logger.info("%-25s : %s", k, v)
        logger.info("Run ID  : %s", run_id)
        logger.info("Run URL : %s", run_url)
        logger.info("=" * 20 + " Evaluation COMPLETED " + "=" * 20)

        return summary, metrics_df, run_id, run_url

    except Exception as e:
        logger.error("Evaluation FAILED - %s", str(e))
        raise e