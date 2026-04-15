import asyncio
import random
import socket
from typing import List
from .nodes import Node
from ..core.signaling import Message
from ..utils.logger import logger

try:
    import socks  # PySocks
    TOR_AVAILABLE = True
except ImportError:
    TOR_AVAILABLE = False


class Router:
    """
    Simulates a network router with optional real TOR routing.
    """

    def __init__(self, nodes: List[Node], use_tor: bool = False):
        self.nodes = {node.node_id: node for node in nodes}
        self.use_tor = use_tor and TOR_AVAILABLE

        if use_tor and not TOR_AVAILABLE:
            logger.warning("PySocks not installed. Falling back to simulation mode.")

    async def route_message(self, message: Message, hops: int = 3):
        """
        Routes a message either:
        - Through simulated multi-hop nodes
        - OR through TOR network if enabled
        """

        if self.use_tor:
            await self._route_via_tor(message)
        else:
            await self._route_simulated(message, hops)

    async def _route_simulated(self, message: Message, hops: int):
        path = self._generate_path(
            message.source_node,
            message.destination_node,
            hops
        )

        logger.info(f"[SIM] Routing {message.message_id} via nodes: {path}")

        onion_payload = self._wrap_onion_layers(message, path)

        for node_id in path:
            node = self.nodes.get(node_id)
            if node:
                await asyncio.sleep(random.uniform(0.1, 0.5))
                onion_payload = await node.receive(onion_payload)

    async def _route_via_tor(self, message: Message):
        """
        Sends the message through TOR SOCKS proxy.
        """
        logger.info(f"[TOR] Routing {message.message_id} via TOR network")

        try:
            sock = socks.socksocket()
            sock.set_proxy(socks.SOCKS5, "127.0.0.1", 9050)

            # Example: connect to destination node address
            destination = self.nodes.get(message.destination_node)

            if not destination:
                logger.error("Destination node not found")
                return

            # Assuming node has host/port attributes
            sock.connect((destination.host, destination.port))

            # Send serialized message
            sock.sendall(message.serialize())

            sock.close()

        except Exception as e:
            logger.error(f"TOR routing failed: {e}")

    def _generate_path(self, source: str, destination: str, hops: int) -> List[str]:
        intermediate_nodes = list(self.nodes.keys())
        intermediate_nodes = [n for n in intermediate_nodes if n not in (source, destination)]
        random.shuffle(intermediate_nodes)

        chosen_hops = intermediate_nodes[:hops]
        return [source] + chosen_hops + [destination]

    def _wrap_onion_layers(self, message: Message, path: List[str]):
        """
        Simulates onion encryption by wrapping payload per hop.
        """
        payload = message

        for node_id in reversed(path):
            payload = {
                "next": node_id,
                "data": payload
            }

        return payload
