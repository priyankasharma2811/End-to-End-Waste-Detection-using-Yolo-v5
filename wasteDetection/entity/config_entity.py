import os
from dataclasses import dataclass
from datetime import datetime

from wasteDetection.constant.traning_pipeline import *

@dataclass  # access data variables instead of cell

class TrainingPipelineConfig:
    artifacts_dir: str = ARTIFACTS_DIR

training_pipeline_config: TrainingPipelineConfig=TrainingPipelineConfig()

# artificats/data_ingestion (it will create artificats inside data ingestion where data will be ingested)
@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, DATA_INGESTION_DIR_NAME
    )

    feature_store_file_path: str = os.path.join(
        data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR
    )

    data_download_url: str = DATA_DOWNLOAD_URL



