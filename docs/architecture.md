# Secure SS7 Simulator Architecture

## Overview

The Secure SS7 Simulator is a legal, safe simulation of signaling networks inspired by the SS7 protocol.  
It is designed to:

1. Simulate node-to-node signaling messages.
2. Encrypt all messages using secure cryptography.
3. Notify users of all simulated communication events.
4. Provide modular components for extensibility and testing.

> **Note:** This project is **educational and research-focused** and does **not interface with real telecom networks**.

---

## System Components

```text
User Interface
      │
      ▼
Notification System ──┐
      │               │
      ▼               │
Event Logger           │
      │               ▼
Signaling Core ──> Network Layer ──> Simulated Nodes
      │
      ▼
Configuration & Helpers
