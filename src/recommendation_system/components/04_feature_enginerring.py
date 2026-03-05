from pathlib import Path
from dataclasses import dataclass
import pickle
import regex as re
from nltk.corpus import stopwords
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np
from src.recommendation_system.entity import feature_enginerring_config
from src.recommendation_system.logging import logger

class feature_enginerring_config:

    def __init__(self, config) -> None:
        self.config = config

    def clean_product_name(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            def clean_text(text):
                if pd.isna(text) or text == '':
                    return ''
                text = str(text).lower()
                text = re.sub(r"'s\b", '', text)
                text = re.sub(r'''\bmen's\b''', 'men', text)
                text = re.sub(r'''\bMen's\b''', 'men', text)
                text = re.sub(r'\bwomens\b', 'women', text)
                text = re.sub(r'\bboys\b', 'boy', text)
                text = re.sub(r'\bgirls\b', 'girl', text)
                text = text.replace('t-shirts', 'tshirts')
                text = text.replace('t-shirt', 'tshirt')
                text = re.sub(r'\(.*?\)', '', text)
                text = re.sub(r'\[.*?\]', '', text)
                text = re.sub(r'\d+', '', text)
                text = re.sub(r'[^a-zA-Z\s]', ' ', text)
                text = re.sub(r'\s+', ' ', text).strip()
                return text

            df['product_name_clean'] = df['product_name'].apply(clean_text)
            logger.info("[Step 1] DONE | shape=%s", df.shape)
            return df

        except Exception as e:
            logger.error("[Step 1] FAILED — %s", str(e))
            raise e

    def extract_url_title(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            garbage_words = [
                'orng', 'mustrd', 'blk', 'twrt',
                'rawenergy', 'newyorkk', 'amour', 'leo'
            ]

            def parse_url(url):
                if pd.isna(url) or url == '':
                    return ''
                try:
                    match = re.search(r'amazon\.in\/([^/]+)\/dp\/', url)
                    if match:
                        title = match.group(1)
                        title = re.sub(r'%[A-Fa-f0-9]{2}', ' ', title)
                        title = re.sub(r'([a-z])([A-Z])', r'\1 \2', title)
                        title = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', title)
                        title = title.replace('T-Shirts', 'Tshirts')
                        title = title.replace('T-Shirt', 'Tshirt')
                        title = title.replace('-', ' ')
                        title = title.replace('_', ' ')
                        title = title.lower()
                        for word in garbage_words:
                            title = re.sub(rf'\b{word}\b', '', title)
                        title = re.sub(r'\bfs\d*\b', '', title)
                        title = re.sub(r'\b[a-z]{1,2}\d+[a-z]*\b', '', title)
                        title = re.sub(r'\b\d+[a-z]+\b', '', title)
                        title = re.sub(r'[^a-zA-Z\s]', ' ', title)
                        title = re.sub(r'\b[a-zA-Z]{1,2}\b', '', title)
                        words = title.split()
                        seen = []
                        for word in words:
                            if word not in seen:
                                seen.append(word)
                        title = ' '.join(seen)
                        title = re.sub(r'\s+', ' ', title).strip()
                        return title
                    return ''
                except Exception as e:
                    logger.warning("[Step 2] URL parse failed  %s", str(e))
                    return ''

            df['url_title'] = df['product_link'].apply(parse_url)
            logger.info("[Step 2] DONE | empty=%d", df['url_title'].eq('').sum())
            return df

        except Exception as e:
            logger.error("[Step 2] FAILED — %s", str(e))
            raise e

    def build_rich_text(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            df['rich_text'] = df['product_name_clean'] + ' ' + df['url_title']
            df['rich_text'] = df['rich_text'].str.replace(
                r'\s+', ' ', regex=True
            ).str.strip()
            logger.info("[Step 3] DONE | shape=%s", df.shape)
            return df

        except Exception as e:
            logger.error("[Step 3] FAILED — %s", str(e))
            raise e

    def remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            before = len(df)
            df = df.sort_values('review_count', ascending=False)
            df = df.drop_duplicates(subset=['rich_text'], keep='first')
            df = df.reset_index(drop=True)
            logger.info("[Step 4] DONE | %d  %d", before, len(df))
            return df

        except Exception as e:
            logger.error("[Step 4] FAILED — %s", str(e))
            raise e

    def build_tfidf(self, df: pd.DataFrame):
        try:
            tfidf = TfidfVectorizer(
                ngram_range=(1, 2),
                min_df=2,
                max_df=0.9
            )
            X = tfidf.fit_transform(df['rich_text'])
            logger.info("[Step 5] DONE  shape=%s  vocab=%d", X.shape, len(tfidf.vocabulary_))
            return X, tfidf

        except Exception as e:
            logger.error("[Step 5] FAILED  %s", str(e))
            raise e

    def build_similarity(self, X) -> np.ndarray:
        try:
            sim_matrix = cosine_similarity(X)
            logger.info("[Step 6] DONE  shape=%s", sim_matrix.shape)
            return sim_matrix

        except Exception as e:
            logger.error("[Step 6] FAILED — %s", str(e))
            raise e

    def build_numerical_score(self, df: pd.DataFrame):
        try:
            scaler = MinMaxScaler()
            df['rating_norm'] = scaler.fit_transform(df[['rating']])
            df['review_norm'] = scaler.fit_transform(df[['review_count']])
            df['score'] = (
                0.4 * df['rating_norm'] +
                0.3 * df['review_norm'] +
                0.2 * (df['discount'] / 100) +
                0.1 * (1 - df['is_new_product'])
            )
            logger.info("[Step 7] DONE min=%.3f max=%.3f", df['score'].min(), df['score'].max())
            return df, scaler

        except Exception as e:
            logger.error("[Step 7] FAILED  %s", str(e))
            raise e

    def initiate_feature_engineering(self):
        try:
            logger.info("=" * 20 + " Feature Engineering STARTED " + "=" * 20)

            df = pickle.load(open(self.config.transformed_model, 'rb'))
            logger.info("Loaded | shape=%s", df.shape)

            df             = self.clean_product_name(df)
            df             = self.extract_url_title(df)
            df             = self.build_rich_text(df)
            df             = self.remove_duplicates(df)
            X, tfidf       = self.build_tfidf(df)
            sim_matrix     = self.build_similarity(X)
            df, scaler     = self.build_numerical_score(df)

            # save — one of each
            pickle.dump(sim_matrix, open(self.config.sim_matrix_path, 'wb'))
            pickle.dump(tfidf,      open(self.config.tfidf_path,      'wb'))
            pickle.dump(scaler,     open(self.config.scaler_path,     'wb'))
            pickle.dump(df,         open(self.config.featured_df_path,'wb'))

            logger.info("Saved sim_matrix  %s", self.config.sim_matrix_path)
            logger.info("Saved tfidf       %s", self.config.tfidf_path)
            logger.info("Saved scaler      %s", self.config.scaler_path)
            logger.info("Saved df          %s", self.config.featured_df_path)
            logger.info("=" * 20 + " Feature Engineering COMPLETED " + "=" * 20)

        except Exception as e:
            logger.error("Feature Engineering FAILED  %s", str(e))
            raise e

