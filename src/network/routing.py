# src/network/routing.py

import asyncio
import random
from typing import List
from .nodes import Node
from ..core.signaling import Message
from ..utils.logger import logger

class Router:
    """
    Simulates a network router that can deliver messages through multiple nodes.
    Can simulate TOR-like multi-hop routing safely.
    """
    def __init__(self, nodes: List[Node]):
        self.nodes = {node.node_id: node for node in nodes}

    async def route_message(self, message: Message, hops: int = 3):
        """
        Routes a message through a randomized path of nodes (simulating multi-hop routing).

        Args:
            message (Message): The message to route.
            hops (int): Number of intermediate hops before reaching the destination.
        """
        path = self._generate_path(message.source_node, message.destination_node, hops)
        logger.info(f"Routing message {message.message_id} via nodes: {path}")

        for node_id in path:
            node = self.nodes.get(node_id)
            if node:
                # Simulate network delay
                await asyncio.sleep(random.uniform(0.1, 0.5))
                await node.receive(message)

    def _generate_path(self, source: str, destination: str, hops: int) -> List[str]:
        """
        Generates a randomized path from source to destination through available nodes.
        """
        intermediate_nodes = list(self.nodes.keys())
        # Remove source and destination
        intermediate_nodes = [n for n in intermediate_nodes if n not in (source, destination)]
        random.shuffle(intermediate_nodes)

        # Take only as many as hops
        chosen_hops = intermediate_nodes[:hops]
        return [source] + chosen_hops + [destination]
