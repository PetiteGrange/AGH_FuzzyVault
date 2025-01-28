import numpy as np
import hashlib
import random

def generate_polynomial(secret: str):

    coefficients = []

    #TODO: ask about the secret
    if not secret:
        raise ValueError("The secret cannot be empty")
    
    #TODO: rework the secret system
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
            

def generate_genuine_points(coefficients, features: str):
    genuine_points = []
    for x in features:
        # Evaluate the polynomial at x
        y = sum(c * (x ** i) for i, c in enumerate(coefficients))  # P(x) = c0 + c1*x + c2*x^2 + ...
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