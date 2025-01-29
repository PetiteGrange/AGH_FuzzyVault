import random
import string
import nltk
from nltk.corpus import words
from src.fuzzyvault import *
import argparse



def main():
    parser = argparse.ArgumentParser(description="Create or decode a vault")
    parser.add_argument('-v', '--vault', type=str, help='Vault file name')
    parser.add_argument('-c', '--create', action='store_true', help='Create a new vault')
    parser.add_argument('-d', '--decode', action='store_true', help='Decode an existing vault')
    parser.add_argument('-l', '--list', action='store_true', help='List all vaults in the "vaults/" directory')
    parser.add_argument('--secret', type=str, help='Custom secret to store in the vault (optional)')
    parser.add_argument('--length', type=int, default=20, help='Length of the secret to generate (default: 20)')

    args = parser.parse_args()

    if args.list:
        list_vaults()
    elif args.create:
        if not args.vault:
            print("You must specify a vault name with --vault when creating a new vault.")
        else:
            create_vault(args.vault, length=args.length, secret=args.secret)
    elif args.decode:
        if not args.vault:
            print("You must specify a vault name with --vault when decoding a vault.")
        else:
            decode_vault(args.vault)
    else:
        print("Please specify a valid action: --create, --decode, or --list.")


if __name__ == "__main__":
    main()
