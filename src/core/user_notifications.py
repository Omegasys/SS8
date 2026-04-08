# src/core/user_notifications.py

from ..utils.logger import logger
from rich.console import Console
import requests

console = Console()

def notify_event(message_id: str, source: str, destination: str, event_type: str, webhook_url: str = None):
    """
    Notify the user of a signaling event.
    
    Args:
        message_id (str): Unique ID of the message.
        source (str): Source node of the message.
        destination (str): Destination node of the message.
        event_type (str): Type of event (e.g., MESSAGE_SENT, MESSAGE_RECEIVED).
        webhook_url (str, optional): If provided, send a POST request to this URL with event data.
    """
    # Prepare the notification message
    msg = f"[{event_type}] Message ID: {message_id}, From: {source}, To: {destination}"
    
    # Console notification
    console.print(msg, style="bold green" if event_type == "MESSAGE_RECEIVED" else "bold blue")
    
    # Log the event
    logger.info(msg)
    
    # Optional: send to webhook
    if webhook_url:
        try:
            payload = {
                "message_id": message_id,
                "source": source,
                "destination": destination,
                "event_type": event_type
            }
            response = requests.post(webhook_url, json=payload, timeout=2)
            if response.status_code != 200:
                logger.warning(f"Webhook notification failed with status code {response.status_code}")
        except Exception as e:
            logger.error(f"Webhook notification error: {e}")
