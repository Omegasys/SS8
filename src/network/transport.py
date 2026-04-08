# src/network/transport.py

import asyncio
import random
from ..core.signaling import Message
from ..utils.logger import logger

class Transport:
    """
    Simulated transport layer for delivering messages between nodes.
    This is fully sandboxed and asynchronous.
    """

    def __init__(self, router):
        """
        Args:
            router: Router object that determines message paths.
        """
        self.router = router

    async def send(self, message: Message, hops: int = 3):
        """
        Sends a message using the router, simulating network transport.

        Args:
            message (Message): Message to deliver.
            hops (int): Number of intermediate hops for the message.
        """
        # Simulate network delay before sending
        delay = random.uniform(0.1, 0.5)
        logger.info(f"Transport: preparing to send message {message.message_id} with {delay:.2f}s delay")
        await asyncio.sleep(delay)

        # Use the router to deliver the message through nodes
        await self.router.route_message(message, hops=hops)
        logger.info(f"Transport: message {message.message_id} delivered to {message.destination_node}")
