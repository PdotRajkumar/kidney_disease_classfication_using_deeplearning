import logging
import os
import sys


log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

logfile_path = os.path.join(log_dir, "running_logs.log")


logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(levelname)s: %(module)s: %(message)s:',
    handlers=[logging.FileHandler(logfile_path),
              logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger("cnnClassifier")