import pandas as pd
from src.logger import logger

def load_data(path: str):
    try:
        logger.info("Loading dataset...")
        df = pd.read_csv(path)

        logger.info(f"Available columns: {list(df.columns)}")

        # Use 'summary' as abstract
        if "summary" not in df.columns:
            raise ValueError("Required column 'summary' not found in dataset")

        # Rename for pipeline consistency
        df = df.rename(columns={"summary": "abstract"})

        # Drop empty abstracts
        df = df.dropna(subset=["abstract"])

        logger.info("Using 'summary' column as abstract")
        logger.info(f"Final dataset size: {len(df)}")

        return df

    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise
