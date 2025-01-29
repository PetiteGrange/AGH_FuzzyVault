from scr.utils import *
import nltk
import textwrap
from nltk.corpus import words

from scr.polynomial import *



def main():

    # Download the words corpus if not already installed
    nltk.download("words")

    # Load the corpus into a dictionary {word: index}
    CORPUS = {word.lower(): i for i, word in enumerate(words.words())}


def run():

    secret = open("datas/passwords.txt", "r")
    features = []

    # Step 1: Generate polynomial
    coefficients = generate_polynomial(secret)

    # Step 2: Generate genuine points
    genuine_points = generate_genuine_points(coefficients, features)

    # Step 3: Add chaff points
    vault = add_chaff_points(genuine_points, num_chaff=10, x_range=(6, 20), y_range=(0, 5000))