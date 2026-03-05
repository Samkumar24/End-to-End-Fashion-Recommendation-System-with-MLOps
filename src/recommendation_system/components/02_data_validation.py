from src.recommendation_system.utils.common import read_yaml , create_dir
from src.recommendation_system.logging import logger
from src.recommendation_system.constants import CONFIG_PATH
from src.recommendation_system.logging import logger
from src.recommendation_system.entity import Data_validation_config
import requests
import os
import pandas as pd
from datetime import datetime

class Data_validation_check:

    def __init__(self, config: Data_validation_config):
        # store config so all methods can use it
        self.config = config

    # ── check 1 — schema ──────────────────────────────────
    def check_schema(self, df):

        # what columns you expect from config.yaml
        expected_columns = self.config.expected_columns

        # what columns actually arrived in new data
        received_columns = list(df.columns)

        # columns present in expected but missing in new data
        # eg: scraper stopped collecting discount column
        missing_columns = [
            col for col in expected_columns
            if col not in received_columns
        ]

        # columns present in new data but not expected
        # eg: scraper added a new column you dont know about
        extra_columns = [
            col for col in received_columns
            if col not in expected_columns
        ]

        return missing_columns, extra_columns

    # ── check 2 — missing values ──────────────────────────
    def check_missing_val(self, df):

        errors = []

        # loop through each column and its allowed threshold
        # eg: rating allows max 45% missing
        for col, threshold in self.config.missing_thresholds.items():

            missing_pct = df[col].isna().mean()

            # if actual missing is above allowed threshold
            if missing_pct > threshold:
                errors.append(
                    f"{col}: {missing_pct:.1%} missing - exceeds {threshold:.1%}"
                )

        # empty list means all columns passed
        return errors

    # ── check 3 — volume ──────────────────────────────────
    def check_volume(self, df):

        # actual number of rows that arrived
        rows = len(df)

        # min and max rows allowed from config.yaml
        min_rows = self.config.volume['min_rows']
        max_rows = self.config.volume['max_rows']

        # 0 rows means scraper completely failed
        # website was down or scraper crashed
        if rows == 0:
            return f"0 rows - scraper completely failed"

        # too few rows means scraper partially failed
        # amazon may have blocked some requests
        if rows < min_rows:
            return f"Too few rows: {rows} - minimum is {min_rows}"

        # too many rows means scraper ran twice
        # every product duplicated
        if rows > max_rows:
            return f"Too many rows: {rows} - maximum is {max_rows}"

        # None means no error - row count is normal
        return None

    # ── check 4 — categories ──────────────────────────────
    def check_categories(self, df):

        # your 7 known aesthetics from config.yaml
        valid = set(self.config.valid_aesthetics)

        # unique aesthetics found in new data
        # dropna removes missing values before checking
        found = set(df['aesthetic'].dropna().unique())

        unseen = found - valid

        if unseen:
            return f"Unseen aesthetics: {unseen}"

        # None means all aesthetics are known
        return None

    # ── check 5 — ranges ──────────────────────────────────
    def check_ranges(self, df):

        errors = []

        # loop through each column and its min/max bounds
        for col, bounds in self.config.range_checks.items():

            # skip if column not present
            # check 1 already caught that
            if col not in df.columns:
                continue

            # ignore missing values when checking range
            col_data = df[col].dropna()

            # find rows where value is below min OR above max
            out_of_range = col_data[
                (col_data < bounds['min']) |
                (col_data > bounds['max'])
            ]

            # if any rows found outside range add to errors
            if len(out_of_range) > 0:
                errors.append(
                    f"{col}: {len(out_of_range)} rows out of range "
                    f"({bounds['min']} - {bounds['max']})"
                )

        # empty list means all columns passed range check
        return errors
    
    def validate_data(self):
        try:
            logger.info("=" * 40)
            logger.info("DATA VALIDATION STARTED")
            logger.info("=" * 40)

            # load raw data from path in config
            # no hardcoding - path comes from config.yaml
            df = pd.read_csv(self.config.raw_data_path)
            logger.info(f"Loaded: {len(df)} rows from {self.config.raw_data_path}")
            logger.info("-" * 40)

            # ── check 1 ───────────────────────────────────
            logger.info("CHECK 1 - SCHEMA")
            missing_col, extra_col = self.check_schema(df)

            # missing columns = hard failure
            # no point running other checks
            if missing_col:
                logger.error(f"FAILED - Missing columns: {missing_col}")
                self.save_log("FAILED", len(df), [f"Missing columns: {missing_col}"])
                return False

            # extra columns = just a warning, not a failure
            if extra_col:
                logger.warning(f"WARNING - Extra columns: {extra_col}")

            logger.info("PASSED - Check 1 Schema")
            logger.info("-" * 40)

            # ── check 2 ───────────────────────────────────
            logger.info("CHECK 2 - MISSING VALUES")
            missing_errors = self.check_missing_val(df)

            # any column above threshold = failure
            if missing_errors:
                for e in missing_errors:
                    logger.error(f"FAILED - {e}")
                self.save_log("FAILED", len(df), missing_errors)
                return False

            logger.info("PASSED - Check 2 Missing Values")
            logger.info("-" * 40)

            # ── check 3 ───────────────────────────────────
            logger.info("CHECK 3 - VOLUME")
            volume_error = self.check_volume(df)

            # returns string if problem, None if ok
            if volume_error:
                logger.error(f"FAILED - {volume_error}")
                self.save_log("FAILED", len(df), [volume_error])
                return False

            logger.info(f"PASSED - Check 3 Volume - {len(df)} rows")
            logger.info("-" * 40)

            # ── check 4 ───────────────────────────────────
            logger.info("CHECK 4 - CATEGORIES")
            category_error = self.check_categories(df)

            # unknown category = warning not failure
            if category_error:
                logger.warning(f"WARNING - {category_error}")
            else:
                logger.info("PASSED - Check 4 Categories")

            logger.info("-" * 40)
            # ── check 5 ───────────────────────────────────
            logger.info("CHECK 5 - RANGES")
            range_errors = self.check_ranges(df)

            # any value outside logical bounds = failure
            if range_errors:
                for e in range_errors:
                    logger.error(f"FAILED - {e}")
                #self.save_log("FAILED", len(df), range_errors)
                return False

            logger.info("PASSED - Check 5 Ranges")
            logger.info("-" * 40)
        


            logger.info("PASSED - Check 5 Ranges")
            logger.info("-" * 40)

            # all checks passed
            # now save the data
            logger.info("Saving validated data...")



            timestamp   = datetime.now().strftime("%Y_%m_%d")
            weekly_path = os.path.join(
            self.config.validated_data,
            f"validated_{timestamp}.csv"
        )
            df.to_csv(weekly_path, index=False)
            logger.info(f"Weekly data saved: validated_{timestamp}.csv")

            master_path = os.path.join(self.config.validated_data,'Master_data.csv')

            if os.path.exists(master_path):
                existing_df = pd.read_csv(master_path)
                combined_df = pd.concat(
                    [existing_df, df],
                    ignore_index=True
                )

                combined_df = combined_df.drop_duplicates(
                    subset='asin',keep='last'
                )
                combined_df.to_csv(master_path, index=False)  # ← add this
                logger.info(f"Master updated: {len(combined_df)} rows")
                

            else:
                comdined_df = df
                comdined_df.to_csv(master_path,index=False)
                logger.info(f"Master created: {len(combined_df)} rows")

            fallback_name = f"fallback_{timestamp}.csv"
            fallback_path = os.path.join(
                self.config.fallback_data,
                fallback_name
        )
            combined_df.to_csv(fallback_path, index=False)
            logger.info(f"Fallback saved: {fallback_name}")
        except Exception as e:
            logger.error(f"Error: {e}")

            