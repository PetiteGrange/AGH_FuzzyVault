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


def calculate_polynomial_degree(secret_length):
    """
    Calculate the degree of the polynomials

    Args:
        secret_length (int): The length of the secret=
    
    Returns:
        int: the degree of the polynomial
    
    """
    # Set a reasonable maximum degree to prevent PC explosion
    min_degree = 3
    max_degree = 10
    degree = min(max_degree, max(min_degree, secret_length // 5))
    return degree


def generate_features(degree):
    """
    Generate a certain amount of words for the features according to the degree if the polynomial

    Args:
        degree (int): the degree of the polynomial
    
    Returns:
        [str]: the features
    
    """
    word_list = words.words()
    
    # Select `degree` number of random words
    selected_words = random.sample(word_list, degree)
    print (selected_words)
    
    return selected_words