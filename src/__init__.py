# src/__init__.py

"""
Secure SS7 Simulator Package
----------------------------

This package simulates a secure SS7-like signaling network
for research and educational purposes. It is fully sandboxed
and does not interact with real telecom networks.

Modules:
- core: Signaling core, encryption, and user notifications
- network: Simulated nodes, routing, and transport
- utils: Configuration, logging, and helper functions
"""

# Expose core modules
from .core.signaling import SignalingCore
from .core.encryption import encrypt_payload, decrypt_payload
from .core.user_notifications import notify_event

# Expose network modules
from .network.nodes import Node
from .network.routing import Router
from .network.transport import Transport

# Expose utilities
from .utils.config import load_config
from .utils.logger import logger

# Optional: set package-level metadata
__version__ = "0.1.0"
__author__ = "Omega"
__license__ = "GPLv3"
