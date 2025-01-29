import random
import hashlib
import string
import nltk
from nltk.corpus import words
from src import *

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



def generate_secret(length=20):
    """
    Generate a random secret to be stored in the fuzzy vault

    Args:
        length (int): The length of the secret, default to 20
    
    Returns:
        str: the secret

    """

    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))