# Secure SS7 Simulator Protocols

## Overview

This document defines the **simulated signaling protocol** used in the Secure SS7 Simulator.  
All protocols are **safe and educational**, designed for research and simulation purposes.

The protocol is inspired by SS7 but **does not interact with real telecom networks**.  
It focuses on **message structure, encryption, routing, and notifications**.

---

## Message Structure

Each message in the simulation follows a structured format:

| Field             | Type        | Description |
|------------------|------------|-------------|
| `message_id`      | UUID       | Unique identifier for the message |
| `source_node`     | String     | Identifier of the sending node |
| `destination_node`| String     | Identifier of the receiving node |
| `timestamp`       | ISO8601    | Time message was created |
| `payload`         | Bytes      | Encrypted message content |
| `signature`       | Bytes      | Digital signature or HMAC for integrity |
| `type`            | String     | Message type (e.g., CALL_SETUP, SMS, DATA) |

> All payloads are encrypted using the **Security Layer**, and each message is signed for integrity.

---

## Encryption Workflow

1. **Message Creation:** The `Signaling Core` constructs a message object with the required fields.
2. **Payload Encryption:**  
   - Symmetric encryption (AES-256) for content.
   - Asymmetric encryption (RSA/ECC) can be optionally used for key exchange.
3. **Integrity Verification:**  
   - HMAC or digital signature is applied to the message.
4. **Routing:**  
   - Encrypted messages are passed to the `Network Layer` for delivery to the destination node.

### Example (Simulation)

```python
from core.signaling import Message, encrypt_payload

msg = Message(
    source_node="NodeA",
    destination_node="NodeB",
    payload="Test signaling message",
    type="CALL_SETUP"
)

encrypted_msg = encrypt_payload(msg.payload)
msg.payload = encrypted_msg
msg.signature = msg.sign()
