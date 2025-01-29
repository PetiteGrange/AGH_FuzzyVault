import random
from src.utils import *


def generate_genuine_points(coefficients: int, features: str):
    """
    Generates genuine points containing the data

    Returns:
        [int, int]: coordinates of genuine points    
    """

    assert len(coefficients) > 0, "Secret coefficients must not be empty."

    genuine_points = []

    #BUG: Un point en trop?

    # Generate more strings from the features
    splited_features = split_features(features)

    # Merge features and splited features to add more points
    features_redundancy = features + splited_features

    for feature in features_redundancy:
        # Hash the word to get a feature value (x-coordinate)
        x = hash_word(feature)

        if x not in [point[0] for point in genuine_points]:

            y = sum(coefficient * (x ** idx) for idx, coefficient in enumerate(coefficients))

            genuine_points.append([x, y])


    return genuine_points


def generate_chaff_points(genuine_x:int, degree:int,points:int = 200, MinX:int = 0, MaxX:int = 9999):
    """
    Function to generate the chaff points to confuse an attacker


    Returns:
        [int, int]: coordinates of chaff points
    
    """

    chaff_points = [] 

    for i in range(points):

        while True:
            # Generate a random x coordinate for the chaff point
            x_fake = random.randint(MinX, MaxX)

            # If it it not in the genuine points, we generate its y based on random coefficients, else we loop arround to generate another x
            if x_fake not in genuine_x:
                random_coefficients = [random.randint(1, 10) for _ in range(degree)]
                y_fake = sum(c * (x_fake ** idx) for idx, c in enumerate(random_coefficients))  

                chaff_points.append([x_fake, y_fake])
                break
    
    return chaff_points

# Function to recover the genuine points using the entered featured by the user
def retrieve_genuine_points(vault: int, features: string):

    points_x = []

    # Add the splited features like during the generation to include more points
    splited_features = split_features(features)
    features_redundancy = splited_features + features

    # hash the features
    for feature in features_redundancy:
        # Hash the word to get a feature value (x-coordinate)
        x = hash_word(feature)
        
        points_x.append(x)

    # get all genuine points corresponding to the features
    genuine_points = [point for point in vault if point[0] in points_x]
    return genuine_points
