import logging

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler("boat.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
