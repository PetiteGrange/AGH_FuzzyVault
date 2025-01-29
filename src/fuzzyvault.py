from src.utils import *
import os
from src.polynomial import *
from src.points import *
import json



def create_vault(vault_name, secret=None, length=20):

    # Make sure that the folder vaults exists
    if not os.path.exists('vaults'):
        os.makedirs('vaults')    

    # Generate the secret
    if secret: secret_to_store = secret
    else: secret_to_store = generate_secret(length)

    # Actualizing the true length
    length = len(secret_to_store)

    # Generate the polynomials coefficients
    degree = calculate_polynomial_degree(len(secret)) # degree of the polynomial
    coefficients = generate_polynomial(secret, degree) #list of coefficients from 0 to last

    print("Coefficients: ", coefficients)
    print("Degree: ", degree)

    # Generation of the features
    features = generate_features(degree)

    print("Features: ", features)

    # Generation of the genuine points
    genuine_points = generate_genuine_points(coefficients, features)

    genuine_x = [point[0] for point in genuine_points]

    # Generation of the chaff points
    chaff_points = generate_chaff_points(genuine_x, degree)

    vault = genuine_points + chaff_points
    random.shuffle(vault)

    # Saving the vault
    vault_path = os.path.join('vaults', vault_name)
    with open(vault_path, 'w') as f:
        json.dump(vault, f)

    # Saving the features
    features_path = os.path.join('features', vault_name + "_f")
    with open(features_path, 'w') as f:
        json.dump(features, f)
    
    print(f"Vault '{vault_name}' created with secret of length {length}: {secret_to_store}")



# Function to decode an existing vault
def decode_vault(vault_name):
    if not os.path.exists(vault_name):
        print(f"Vault '{vault_name}' does not exist.")
        return
    
    with open(vault_name, 'r') as f:
        secret = f.read().strip()
    
    print(f"Decoded secret from vault '{vault_name}': {secret}")



def list_vaults():

    # Make sure that the folder vaults exists
    if not os.path.exists('vaults'):
        os.makedirs('vaults')

    vault_files = [f for f in os.listdir('vaults') if os.path.isfile(os.path.join('vaults', f))]
    
    if vault_files:
        print("Vaults in 'vaults/' directory:")
        for vault in vault_files:
            print(vault)
    else:
        print("No vaults found in 'vaults/'.")