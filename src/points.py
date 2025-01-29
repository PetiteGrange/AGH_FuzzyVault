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

        genuine_points.append([x, y])

    return genuine_points

def generate_chaff_points(genuine_x:int, degree:int,points:int = 200, MinX:int = 0, MaxX:int = 9999):

    chaff_points = [] 

    for i in range(points):
        while True:
            x_fake = random.randint(MinX, MaxX)
            if x_fake not in genuine_x:
                random_coefficients = [random.randint(1, 10) for _ in range(degree)]
                y_fake = sum(c * (x_fake ** idx) for idx, c in enumerate(random_coefficients))  
                chaff_points.append([x_fake, y_fake])
                break
    
    return chaff_points
