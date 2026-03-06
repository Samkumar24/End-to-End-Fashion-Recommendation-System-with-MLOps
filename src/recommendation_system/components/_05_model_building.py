from src.recommendation_system.constants import CONFIG_PATH
from src.recommendation_system.utils.common import read_yaml , create_dir
from dataclasses import dataclass
from src.recommendation_system.logging import logger
import pickle
from src.recommendation_system.entity import model_building_config

class model_building_check:

    def __init__(self, config) -> None:
        self.config = config
        self.sim_matrix = None
        self.df = None

    def load_artifacts(self):
        try:
            logger.info("=" * 20 + " Loading Artifacts STARTED " + "=" * 20)

            with open(self.config.sim_matrix_path, 'rb') as f:
                self.sim_matrix = pickle.load(f)
            with open(self.config.featured_df_path, 'rb') as f:
                self.df = pickle.load(f)

            logger.info("sim_matrix shape : %s", str(self.sim_matrix.shape))
            logger.info("df shape         : %s", str(self.df.shape))
            logger.info("df columns       : %s", list(self.df.columns))
            logger.info("=" * 20 + " Loading Artifacts COMPLETED " + "=" * 20)

            return self.sim_matrix, self.df

        except Exception as e:
            logger.error("Load artifacts FAILED - %s", str(e))
            raise e

    def recommendation_engine_1(self, product_id, n=10):
        # similarity based recommendations
        try:
            scores  = self.sim_matrix[product_id]
            top_idx = scores.argsort()[::-1][1:n+1]
            top_scores = scores[top_idx]

            results = self.df.iloc[top_idx][[
                'product_name_clean',
                'price',
                'rating',
                'aesthetic',
                'score',
            ]].copy()

            results['similarity'] = top_scores

            logger.info("[Engine 1] Top %d similar products found", n)
            logger.info("=" * 20 + " Engine 1 COMPLETED " + "=" * 20)

            return results, top_idx

        except Exception as e:
            logger.error("[Engine 1] FAILED - %s", str(e))
            raise e

    def recommendation_engine_2(self, aesthetic, n=10):
        # aesthetic/category based recommendations
        try:
            filtered = self.df[self.df['aesthetic'] == aesthetic]

            top_products = filtered.sort_values(
                'score', ascending=False
            ).head(n)

            logger.info("[Engine 2] Total in aesthetic : %d", len(filtered))
            logger.info("[Engine 2] Top %d products found", n)
            logger.info("=" * 20 + " Engine 2 COMPLETED " + "=" * 20)

            return top_products

        except Exception as e:
            logger.error("[Engine 2] FAILED - %s", str(e))
            raise e

    def initiate_recommendation(self, product_name, top_k=5):
        try:
            logger.info("=" * 20 + " Recommendation STARTED " + "=" * 20)

            # load artifacts
            self.sim_matrix, self.df = self.load_artifacts()

            # validate product exists
            if product_name not in self.df["product_name_clean"].values:
                raise ValueError(f"Product '{product_name}' not found")

            # get product_id and aesthetic
            product_id = self.df[self.df["product_name_clean"] == product_name].index[0]
            aesthetic  = self.df.loc[product_id, "aesthetic"]

            logger.info("Input product : %s", product_name)
            logger.info("Product ID    : %d", product_id)
            logger.info("Aesthetic     : %s", aesthetic)

            # engine 1 — similarity based
            recs_sim, top_idx = self.recommendation_engine_1(
                product_id=product_id,
                n=top_k
            )

            # engine 2 — aesthetic based
            recs_aesthetic = self.recommendation_engine_2(
                aesthetic=aesthetic,
                n=top_k
            )

            logger.info("=" * 20 + " Recommendation COMPLETED " + "=" * 20)

            return recs_sim, recs_aesthetic

        except Exception as e:
            logger.error("Recommendation FAILED - %s", str(e))
            raise e