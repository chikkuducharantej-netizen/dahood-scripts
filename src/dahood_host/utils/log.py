"""Tiny logger factory used across the Da Hood host."""
from __future__ import annotations

import logging
import sys


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stderr)
        handler.setFormatter(logging.Formatter("[%(asctime)s] %(name)s: %(message)s"))
        logger.addHandler(handler)
        logger.setLevel(level)
    return logger