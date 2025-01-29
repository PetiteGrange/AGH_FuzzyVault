import numpy as np
import hashlib
import random
from src.utils import *


def generate_polynomial(secret: str, degree: int):

    coefficients = []

    # If for some reason the secret is empty
    if not secret:
        raise ValueError("The secret cannot be empty")
    
    
    chunk_size = len(secret) // degree + (len(secret) % degree > 0)
    chunks = [secret[i:i + chunk_size] for i in range(0, len(secret), chunk_size)]


    for chunk_index, chunk in enumerate(chunks):
        # Use SHA-256 to hash the word and convert to an integer
        coef = hash_word(chunk, 10000)
        #print(f"Coefficient {chunk_index} : {coef} from {chunk}")

        # Append the coefficient to the list
        coefficients.append(coef) 

    return coefficients
            

def polynomial_evaluation(x, coefficients):
    """
    Evaluate a polynomial at a specific x using the given coefficients.
    """
    return sum(coeff * (x ** i) for i, coeff in enumerate(coefficients))


