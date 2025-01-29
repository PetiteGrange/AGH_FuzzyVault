import hashlib

def hash_word_to_number(word, mod=1000):
    """
    Convert a word into a numeric value using SHA-256 hashing.
    
    Args:
        word (str): The input word.
        mod (int): The modulus to limit x-coordinate range.
    
    Returns:
        int: A numeric representation of the word.
    """
    return int(hashlib.sha256(word.encode()).hexdigest(), 16) % mod


def split_text(text, chunk_size=6):
    """
    Split a secret into fixed-size chunks.
    
    Args:
        secret (str): The secret string.
        chunk_size (int): Number of characters per chunk.
    
    Returns:
        list of str: Chunks of the secret.
    """
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]