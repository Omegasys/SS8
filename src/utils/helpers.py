# src/utils/helpers.py

import random
import string
from datetime import datetime


def generate_random_node_id(length: int = 6) -> str:
    """
    Generate a random node ID consisting of uppercase letters and digits.

    Args:
        length (int): Length of the node ID. Default is 6.

    Returns:
        str: Random node ID.
    """
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def current_timestamp() -> str:
    """
    Returns the current UTC timestamp in ISO 8601 format.

    Returns:
        str: Current timestamp, e.g., '2026-04-07T12:34:56.789Z'
    """
    return datetime.utcnow().isoformat() + "Z"


def summarize_payload(payload: str, length: int = 20) -> str:
    """
    Returns a short summary of a payload for logging purposes.

    Args:
        payload (str): The message payload.
        length (int): Maximum length of the summary.

    Returns:
        str: Truncated summary of the payload.
    """
    if len(payload) <= length:
        return payload
    return payload[:length] + "..."


def validate_node_id(node_id: str) -> bool:
    """
    Validates that a node ID only contains uppercase letters and digits.

    Args:
        node_id (str): The node ID to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    return all(c.isupper() or c.isdigit() for c in node_id)
