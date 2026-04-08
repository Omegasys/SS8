# Secure SS7 Simulator Security

## Overview

The Secure SS7 Simulator is designed with **security and privacy in mind**, even though it operates entirely in a simulated environment.  
This document describes the **security architecture, encryption practices, and integrity measures** used throughout the system.

> **Note:** This project is purely for educational and research purposes and **does not interact with real telecom networks**.

---

## Security Principles

1. **Confidentiality:** All message payloads are encrypted before transmission.
2. **Integrity:** All messages include a cryptographic signature or HMAC to detect tampering.
3. **Authentication:** Nodes are authenticated before exchanging messages in the simulation.
4. **Auditability:** All events and message activities are logged securely for research and debugging.
5. **Isolation:** Simulation runs in a sandboxed environment, ensuring no accidental real-world exposure.

---

## Encryption

### Symmetric Encryption

- **Algorithm:** AES-256 in GCM mode.
- **Purpose:** Encrypts the payload of each message for confidentiality.
- **Key Management:** Symmetric keys are generated per session or per node pair in the simulation.

### Asymmetric Encryption (Optional)

- **Algorithm:** RSA 2048 / ECC 256-bit
- **Purpose:** Secure key exchange between nodes.
- **Use Case:** Establish session keys for symmetric encryption.

### Example (Simulation)

```python
from core.encryption import encrypt_payload, decrypt_payload

payload = "Simulated signaling message"
encrypted = encrypt_payload(payload)
decrypted = decrypt_payload(encrypted)
