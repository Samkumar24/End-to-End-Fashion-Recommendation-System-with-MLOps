import pandas as pd
import numpy as np
from src.recommendation_system.utils.common import read_yaml , create_dir
from src.recommendation_system.logging import logger
from src.recommendation_system.constants import CONFIG_PATH
from src.recommendation_system.logging import logger
from src.recommendation_system.entity import Data_transformation_config
import pickle
import os
import regex as re


class Data_transformation_check:

    def __init__(self, config:Data_transformation_config):
        # config should contain paths like:
        # config.valid_data
        # config.transformed_data
        self.config = config

    def fix_duplicates(self , df: pd.DataFrame) -> pd.DataFrame:

        logger.info("Data shape : %s", df.shape)
        df = df.drop_duplicates(subset=['asin'])
        df = df.reset_index(drop=True)
        logger.info("Data shape after removing duplicates : %s",df.shape)
        
        return df

    # ── Fix price missing values ─────────────────────────
    def fix_price(self, df: pd.DataFrame) -> pd.DataFrame:
        missing = df['price'].isna().sum()
        median_val = df['price'].median()

        df['price'] = df['price'].fillna(median_val)
        df['price'] = np.log1p(df['price'])
        logger.info(
            "[Price] %d missing median=%.2f",
            missing,
            median_val
        )
        return df

    # ── Fix review_count ────────────────────────────────
    def fix_review_count(self, df: pd.DataFrame) -> pd.DataFrame:

        def parse_review(x):
            if pd.isna(x):
                return 0

            x = str(x).lower().strip()
            try:
                if 'k' in x:
                    return int(float(x.replace('k', '')) * 1000)
                elif 'l' in x:
                    return int(float(x.replace('l', '')) * 100000)
                else:
                    return int(float(x))
            except ValueError:
                return 0

        missing = df['review_count'].isna().sum()
        df['review_count'] = df['review_count'].apply(parse_review)
        df['review_count'] = np.log1p(df['review_count'])

        logger.info(
            "[ReviewCount] %d missing -> filled with 0",
            missing
        )
        return df

# ── Fix discount ────────────────────────────────

    def fix_discount(self , df : pd.DataFrame)->pd.DataFrame :

        missing = df['discount'].isna().sum()
        df['discount'] = df['discount'].apply(lambda x : re.sub(r'[^\d]','',str(x)))
        df['discount'] = df['discount'].replace('', pd.NA)
        df['discount'] = df['discount'].fillna(0)
        df['discount'] = df['discount'].astype('int')
        
        logger.info(
            "[Discount] %d missing -> 0 | range=%d%%–%d%%",
            missing,
            df['discount'].min(),
            df['discount'].max()
        )
        return df
    
    def fix_rating(self, df: pd.DataFrame) -> pd.DataFrame:
        missing = df['rating'].isna().sum()

        # Flag BEFORE any fill — signal lost forever after
        df['is_new_product'] = df['rating'].isna().astype(int)

        # Group median per aesthetic
        # old_money median != y2k_party median
        df['rating'] = df.groupby('aesthetic')['rating'].transform(
            lambda x: x.fillna(x.median())
        )

        logger.info(
            "[Rating] %d missing -> group median | %d new products flagged",
            missing,
            df['is_new_product'].sum()
        )
        return df
    # ── Main transformation logic ───────────────────────
    def get_data_transformer_data(self):

        # Load validated data
        df = pd.read_csv(self.config.valid_data)
        logger.info("Loaded data | shape=%s", df.shape)

        # Before checks
        logger.info("Price missing BEFORE: %d", df['price'].isna().sum())
        logger.info("Review_count missing BEFORE: %d", df['review_count'].isna().sum())

        # Transform
        df = self.fix_duplicates(df)
        df = self.fix_price(df)
        df = self.fix_review_count(df)
        df = self.fix_discount(df)
        df = self.fix_rating(df)

        print(df.isna().sum())

        # After checks (PROOF)
        logger.info("Price missing AFTER: %d", df['price'].isna().sum())
        logger.info("Review_count missing AFTER: %d", df['review_count'].isna().sum())

        # Hard guarantees
        assert df['price'].isna().sum() == 0, "Price still has missing values"
        assert df['review_count'].isna().sum() == 0, "Review count still has missing values"

        
        df_csv_path = os.path.join(self.config.transformed_data,'Transformed_Data.csv')
        df.to_csv(df_csv_path, index=False)
        logger.info("Saved CSV {df_csv_path}%s", self.config.transformed_data)

        # Save PKL — preserves dtypes for next step
        pkl_path = os.path.join(
            self.config.model_path, 'Transformed_Data.pkl'
        )
        pickle.dump(df, open(pkl_path, 'wb'))
        logger.info("Saved PKL - %s", pkl_path)


        

    # ── Pipeline entry point ────────────────────────────
    def initiate_data_transformation(self):
        logger.info("=" * 20 + " Data Transformation STARTED " + "=" * 20)
        self.get_data_transformer_data()
        logger.info("=" * 20 + " Data Transformation COMPLETED " + "=" * 20)