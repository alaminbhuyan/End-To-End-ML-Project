import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
# It will create a logs folder
os.makedirs(log_dir, exist_ok=True)

# logging configuration
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        # It will also print log in terminal so that we specify it
        logging.FileHandler(filename=log_filepath),
        logging.StreamHandler(stream=sys.stdout)
    ]
)

logger = logging.getLogger("mlprojectLogger")