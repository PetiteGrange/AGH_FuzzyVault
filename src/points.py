import random
from src.utils import *



def generate_genuine_points(coefficients: int, features: str, points: int = 20):
    """
    Generates genuine points
    
    """

    assert len(coefficients) > 0, "Secret coefficients must not be empty."

    genuine_points = []

    for i in range(points):
        # Hash the word to get a feature value (x-coordinate)
        word = features[i % len(features)]  # Use modulo to cycle through words
        x = hash_word(word)

        y = sum(coefficient * (x ** idx) for idx, coefficient in enumerate(coefficients))

        genuine_points.append((x, y))

    return genuine_points



    

