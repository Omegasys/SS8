# src/utils/config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env if it exists
load_dotenv()

# Simulator configuration with defaults
CONFIG = {
    "NUM_NODES": int(os.getenv("NUM_NODES", 5)),  # Number of simulated nodes
    "DEFAULT_HOPS": int(os.getenv("DEFAULT_HOPS", 3)),  # Default multi-hop routing
    "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),  # Logging level
    "WEBHOOK_URL": os.getenv("WEBHOOK_URL", None),  # Optional webhook for notifications
}

def load_config():
    """
    Returns the current simulator configuration as a dictionary.
    """
    return CONFIG
