import numpy as np
import hashlib
import random

def generate_polynomial(secret: str):

    coefficients = []

    #TODO: ask about the secret
    if not secret:
        raise ValueError("The secret cannot be empty")
    
    
    #TODO split string
    secret_words = secret.split(" ")
    print("Secret parts: ", secret_words)

    # Define the degree of the polynomial
    degree = len(secret_words) - 1
    print("Degree: ", degree)

    for word_index, word in enumerate(secret_words):
        # Use SHA-256 to hash the word and convert to an integer
        hashed_word = int(hashlib.sha256(word.encode()).hexdigest(), 16)

        # Reduce the hash to a smaller value to use as a coefficient, limit to 1000 so my computer doesn't explode
        coef = hashed_word % 1000
        print(f"Coefficient {word_index} :", coef)

        # Append the coefficient to the list
        coefficients.append(coef) 

    return coefficients
            