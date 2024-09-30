import pandas as pd
import numpy as np

from src.logger.logging import logging
from src.exception.exception import customexception

import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    # Get the absolute path of the project root (assuming the script is inside src/component)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    raw_data_path: str = os.path.join(project_root, "artifacts", "raw.csv")
    train_data_path: str = os.path.join(project_root, "artifacts", "train.csv")
    test_data_path: str = os.path.join(project_root, "artifacts", "test.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("data ingestion started")
        try:
            data = pd.read_csv("https://raw.githubusercontent.com/protickcse22/data-sets/refs/heads/main/gemstone.csv")
            logging.info("reading a df")
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info(" i have saved the raw dataset in artifact folder")

            logging.info("here i have performed train test split")

            train_data, test_data = train_test_split(data, test_size=0.25)
            logging.info("train test split completed")

            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)

            logging.info("data ingestion part completed")

            return (

                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info()
            raise customexception(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()

