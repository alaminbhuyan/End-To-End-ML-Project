from dataclasses import dataclass
from pathlib import Path

# Let's create Data ingestion config

# we used dataclass to specify the return type that we want to return
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    source_URL : str
    local_data_file : Path
    unzip_dir : Path