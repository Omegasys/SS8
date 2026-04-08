# src/core/signaling.py

import asyncio
import uuid
from datetime import datetime

from .encryption import encrypt_payload, decrypt_payload
from .user_notifications import notify_event
from ..utils.logger import logger


class Message:
    """Represents a simulated signaling message."""
    def __init__(self, source_node, destination_node, payload, msg_type="DATA"):
        self.message_id = str(uuid.uuid4())
        self.source_node = source_node
        self.destination_node = destination_node
        self.timestamp = datetime.utcnow().isoformat()
        self.payload = payload
        self.type = msg_type
        self.signature = None

    def sign(self):
        """Generate a simple HMAC-like signature for simulation."""
        # In a real system, this would be a cryptographic signature
        self.signature = f"{self.message_id}-{self.source_node}-{self.destination_node}"
        return self.signature


class SignalingCore:
    """Simulates the core signaling functionality."""
    def __init__(self):
        self.sent_messages = []

    async def send_message(self, message: Message):
        """Simulate sending a message asynchronously."""
        # Encrypt payload
        message.payload = encrypt_payload(message.payload)
        # Sign message
        message.sign()
        # Log the event
        logger.info(f"Message {message.message_id} sent from {message.source_node} to {message.destination_node}")
        self.sent_messages.append(message)
        # Notify user
        notify_event(
            message_id=message.message_id,
            source=message.source_node,
            destination=message.destination_node,
            event_type="MESSAGE_SENT"
        )
        # Simulate network delay
        await asyncio.sleep(0.5)
        # Deliver message
        await self.receive_message(message)

    async def receive_message(self, message: Message):
        """Simulate receiving and processing a message asynchronously."""
        # Decrypt payload
        decrypted_payload = decrypt_payload(message.payload)
        logger.info(f"Message {message.message_id} received at {message.destination_node}. Payload: {decrypted_payload}")
        # Notify user
        notify_event(
            message_id=message.message_id,
            source=message.source_node,
            destination=message.destination_node,
            event_type="MESSAGE_RECEIVED"
        )


async def main():
    """Demo function to run the signaling simulation."""
    signaling_core = SignalingCore()

    # Create a simulated message
    msg = Message(
        source_node="NodeA",
        destination_node="NodeB",
        payload="Hello, this is a secure test message!",
        msg_type="CALL_SETUP"
    )

    # Send the message
    await signaling_core.send_message(msg)


if __name__ == "__main__":
    asyncio.run(main())
