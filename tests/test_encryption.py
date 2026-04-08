# tests/test_encryption.py

import pytest
from src.core.encryption import encrypt_payload, decrypt_payload

def test_encrypt_decrypt_basic():
    payload = "This is a test message."
    
    # Encrypt the payload
    encrypted = encrypt_payload(payload)
    
    # Ensure the output is bytes and different from the original
    assert isinstance(encrypted, bytes)
    assert encrypted != payload.encode('utf-8')
    
    # Decrypt the payload
    decrypted = decrypt_payload(encrypted)
    
    # Ensure decrypted message matches original
    assert decrypted == payload

def test_encrypt_decrypt_empty_string():
    payload = ""
    
    encrypted = encrypt_payload(payload)
    assert isinstance(encrypted, bytes)
    
    decrypted = decrypt_payload(encrypted)
    assert decrypted == payload

def test_encrypt_decrypt_unicode():
    payload = "测试信息 🚀"
    
    encrypted = encrypt_payload(payload)
    assert isinstance(encrypted, bytes)
    
    decrypted = decrypt_payload(encrypted)
    assert decrypted == payload

def test_encrypt_different_messages_produce_different_ciphertexts():
    payload1 = "Message One"
    payload2 = "Message Two"
    
    encrypted1 = encrypt_payload(payload1)
    encrypted2 = encrypt_payload(payload2)
    
    assert encrypted1 != encrypted2
