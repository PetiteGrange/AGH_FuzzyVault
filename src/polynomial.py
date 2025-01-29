import numpy as np
import hashlib
import random
from src.utils import *


def generate_polynomial(secret: str, degree: int):

    coefficients = []

    # If for some reason the secret is empty
    if not secret:
        raise ValueError("The secret cannot be empty")
    
    #TODO: rework the secret system
    chunk_size = len(secret) // degree + (len(secret) % degree > 0)
    chunks = [secret[i:i + chunk_size] for i in range(0, len(secret), chunk_size)]


    for chunk_index, chunk in enumerate(chunks):
        # Use SHA-256 to hash the word and convert to an integer
        hashed_word = int(hashlib.sha256(chunk.encode()).hexdigest(), 16)

        # Reduce the hash to a smaller value to use as a coefficient, limit to 1000 so my computer doesn't explode
        coef = hashed_word % 1000
        print(f"Coefficient {chunk_index} : {coef} from {chunk}")

        # Append the coefficient to the list
        coefficients.append(coef) 

    return coefficients
            

def generate_genuine_points(coefficients, features: str):
    genuine_points = []
    for x in features:
        # Evaluate the polynomial at x
        y = sum(coef * (x ** i) for i, coef in enumerate(coefficients))
        genuine_points.append((x, y))
    return genuine_points


def add_chaff_points(genuine_points, num_chaff, x_range, y_range):

    #TODO Review this code.

    chaff_points = set()
    genuine_x = {x for x, y in genuine_points}
    while len(chaff_points) < num_chaff:
        x = random.randint(*x_range)
        y = random.randint(*y_range)
        if x not in genuine_x:  # Ensure no overlap with genuine points
            chaff_points.add((x, y))
    return list(chaff_points) + genuine_points