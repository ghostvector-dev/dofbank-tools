# utils/logger.py — DofBank Migration Logging Utility

import logging
import os
import sys

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "migration.log")


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # Console handler
        c_handler = logging.StreamHandler(sys.stdout)
        c_format = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        c_handler.setFormatter(c_format)
        logger.addHandler(c_handler)

        # File handler
        f_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
        f_format = logging.Formatter(
            "%(asctime)s [%(levelname)s] [%(name)s] (%(filename)s:%(lineno)d): %(message)s"
        )
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)

    return logger
