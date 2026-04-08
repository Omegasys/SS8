# tests/test_signaling.py

import asyncio
import pytest

from src.core.signaling import SignalingCore, Message
from src.core.encryption import encrypt_payload, decrypt_payload
from src.core.user_notifications import notify_event


@pytest.mark.asyncio
async def test_message_creation():
    msg = Message(source_node="NodeA", destination_node="NodeB", payload="Hello World", msg_type="DATA")
    assert msg.source_node == "NodeA"
    assert msg.destination_node == "NodeB"
    assert msg.payload == "Hello World"
    assert msg.type == "DATA"
    assert msg.message_id is not None

    signature = msg.sign()
    assert signature == msg.signature


@pytest.mark.asyncio
async def test_encryption_decryption():
    payload = "Secret Payload"
    encrypted = encrypt_payload(payload)
    assert isinstance(encrypted, bytes)
    
    decrypted = decrypt_payload(encrypted)
    assert decrypted == payload


@pytest.mark.asyncio
async def test_send_receive_message():
    core = SignalingCore()
    
    msg = Message(source_node="NodeA", destination_node="NodeB", payload="Test Message")
    
    # Patch notify_event to avoid actual console/webhook output
    notifications = []

    def mock_notify(**kwargs):
        notifications.append(kwargs)

    # Replace the real notify_event with our mock
    original_notify = notify_event
    try:
        from src.core import user_notifications
        user_notifications.notify_event = mock_notify

        await core.send_message(msg)
        
        # Check that message was added to sent_messages
        assert msg in core.sent_messages
        
        # Check that notifications were triggered
        sent_notif = any(n['event_type'] == "MESSAGE_SENT" for n in notifications)
        received_notif = any(n['event_type'] == "MESSAGE_RECEIVED" for n in notifications)
        assert sent_notif
        assert received_notif

    finally:
        user_notifications.notify_event = original_notify
