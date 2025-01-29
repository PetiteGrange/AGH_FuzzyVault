from src.utils import *
from sympy import Symbol, interpolate

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


def interpolation(points):
    """
    Interpolates a polynomial through the given points using Lagrange's method.

    Args:
        points (int): List of (x, y) pairs (genuine points)
    
    Returns:
        [int]: Polynomial coefficients
    """

    x_values, y_values = zip(*points)
    x = Symbol('x')
    
    # Interpolating polynomial
    polynomial = interpolate(list(zip(x_values, y_values)), x)

    # Extract the coefficients from the polynomial
    coefficients = [polynomial.coeff(x, i) for i in range(polynomial.as_poly().degree() + 1)]   

    return coefficients
