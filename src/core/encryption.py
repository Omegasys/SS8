# src/core/encryption.py

from cryptography.fernet import Fernet

# Generate a single key for the simulation
# In a real system, keys would be managed per node/session
SIMULATION_KEY = Fernet.generate_key()
fernet = Fernet(SIMULATION_KEY)


def encrypt_payload(payload: str) -> bytes:
    """
    Encrypts the message payload using AES-256 symmetric encryption (Fernet).
    
    Args:
        payload (str): The plaintext message to encrypt.
        
    Returns:
        bytes: Encrypted payload.
    """
    if isinstance(payload, str):
        payload = payload.encode('utf-8')
    encrypted = fernet.encrypt(payload)
    return encrypted


def decrypt_payload(encrypted_payload: bytes) -> str:
    """
    Decrypts the message payload using AES-256 symmetric encryption (Fernet).
    
    Args:
        encrypted_payload (bytes): The encrypted message.
        
    Returns:
        str: Decrypted plaintext message.
    """
    decrypted = fernet.decrypt(encrypted_payload)
    return decrypted.decode('utf-8')
