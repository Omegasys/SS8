# src/network/nodes.py

from typing import Optional
from ..core.signaling import SignalingCore, Message


class Node:
    """
    Represents a simulated network node.
    
    Attributes:
        node_id (str): Unique identifier of the node.
        signaling_core (SignalingCore): Reference to the signaling core used for sending/receiving messages.
    """
    def __init__(self, node_id: str, signaling_core: Optional[SignalingCore] = None):
        self.node_id = node_id
        self.signaling_core = signaling_core or SignalingCore()

    async def send(self, payload: str, destination_node_id: str, msg_type: str = "DATA"):
        """
        Sends a message from this node to another node.
        
        Args:
            payload (str): Message content.
            destination_node_id (str): ID of the destination node.
            msg_type (str, optional): Type of the message (e.g., DATA, CALL_SETUP). Defaults to "DATA".
        """
        msg = Message(
            source_node=self.node_id,
            destination_node=destination_node_id,
            payload=payload,
            msg_type=msg_type
        )
        await self.signaling_core.send_message(msg)

    async def receive(self, message: Message):
        """
        Handles a received message. Can be extended for custom node behavior.
        
        Args:
            message (Message): The message received.
        """
        # By default, just process via the signaling core
        await self.signaling_core.receive_message(message)
