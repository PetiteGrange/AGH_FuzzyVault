from src.utils import *
import nltk
import textwrap
from nltk.corpus import words
import os
from src.polynomial import *



def create_vault(vault_name, secret=None, length=20):

    # Make sure that the folder vaults exists
    if not os.path.exists('vaults'):
        os.makedirs('vaults')

    # Add the vault path
    vault_path = os.path.join('vaults', vault_name)

    # Generate the secret
    if secret: secret_to_store = secret
    else: secret_to_store = generate_secret(length)


    with open(vault_path, 'w') as f:
        f.write(secret_to_store)
    
    print(f"Vault '{vault_name}' created with secret of length {length}: {secret_to_store}")


# Function to decode an existing vault
def decode_vault(vault_name):
    if not os.path.exists(vault_name):
        print(f"Vault '{vault_name}' does not exist.")
        return
    
    with open(vault_name, 'r') as f:
        secret = f.read().strip()
    
    print(f"Decoded secret from vault '{vault_name}': {secret}")