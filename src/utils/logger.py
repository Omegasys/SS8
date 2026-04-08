# src/utils/logger.py

from loguru import logger
import sys

# Remove default handler and configure a standard one
logger.remove()

# Console logging
logger.add(sys.stdout, format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", level="INFO")

# Optional: log to a file (rotates every 5 MB, keeps 3 backups)
logger.add(
    "logs/simulator.log",
    rotation="5 MB",
    retention=3,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO",
    enqueue=True  # thread-safe logging
)

# Example: logger.info("Logger initialized for Secure SS7 Simulator")
