# run_simulation.py

import asyncio
from src.utils.config import load_config
from src.utils.helpers import generate_random_node_id
from src.network.nodes import Node
from src.network.routing import Router
from src.network.transport import Transport
from src.core.signaling import Message

async def main():
    config = load_config()
    num_nodes = config["NUM_NODES"]
    default_hops = config["DEFAULT_HOPS"]
    webhook_url = config["WEBHOOK_URL"]

    print(f"Starting simulation with {num_nodes} nodes and {default_hops} hops per message...\n")

    # Create simulated nodes
    nodes = [Node(node_id=generate_random_node_id()) for _ in range(num_nodes)]

    # Map of node IDs for reference
    node_ids = [node.node_id for node in nodes]
    print(f"Simulated nodes: {node_ids}\n")

    # Initialize router and transport
    router = Router(nodes)
    transport = Transport(router)

    # Send a demo message from first node to last node
    sender = nodes[0]
    receiver = nodes[-1]
    payload = "Hello from the simulation!"
    msg = Message(source_node=sender.node_id, destination_node=receiver.node_id, payload=payload)

    print(f"Sending message from {sender.node_id} to {receiver.node_id}...\n")
    await transport.send(msg, hops=default_hops)

    print("\nSimulation complete.")

if __name__ == "__main__":
    asyncio.run(main())
