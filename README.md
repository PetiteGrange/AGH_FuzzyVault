# AGH_FuzzyVault

## Installation

First clone the repository to your working directory

The project has been develloped on Python 3.12.7

To install the required packages, run the following command:
```sh
pip install -r requirements.txt
```
You are good to go now!


## Usage

First make sure you are in the root of the project


```
usage: main.py [-h] [-v VAULT] [-c] [-d] [-l] [--secret SECRET] [--length LENGTH]

Create or decode a vault

options:
  -h, --help            show this help message and exit
  -v VAULT, --vault VAULT   Vault file name

  -c, --create          Create a new vault
  -d, --decode          Decode an existing vault
  -l, --list            List all vaults in the "vaults/" directory
  --secret SECRET       Custom secret to store in the vault (optional)
  --length LENGTH       Length of the secret to generate (default: 20)
```

### Creating a vault to store a secret

To create a vault you will need to type:

```sh
python main.py -v VAULT_NAME -c
```

You can also personalize the length of the generated secret (```--length INT```) or give a secret you made yourself (```--secret STRING```)

When the vault is created, it will create a file VAULT_NAME in vaults/ containing the encrypted vault and a file VAULT_NAME_f containing the features (passphrase) in features/ . Both of these files are writed in JSON for easier handling.

There is no need to create these two folders.


### Decoding a vault

To decode the vault, you will need your vault file inside the folder vaults/

Then type the command below and write each word of the passphrase, the order isn't important.

```sh
python main.py -v VAULT_NAME -d
```

As it is a fuzzy vault, you can make some mistake or leave out some words and still be able to retrieve the secret.

If you forgot the name of your vault you can retrieve all the current create vault with the command:

```sh
python main.py -l
```


## Inspirations

### Some repos:

This is some Github repositories I read to understand how a fuzzy vault works

- Simple, python, based on original: https://github.com/jwoogerd/fuzzy_vault

- Decentralized, C/C++ : https://github.com/decentralized-identity/fuzzy-encryption

- Thesis, python, seems hard, decentralized: https://github.com/abb-iss/distributed-fuzzy-vault


### Some papers:

This is some papers I read to get familiar with the concept and algorithm

- The original: https://people.csail.mit.edu/madhu/papers/2002/ari-journ.pdf

- On implementation: https://arxiv.org/pdf/2102.02458

- Implementation of encryption: https://github.com/decentralized-identity/fuzzy-encryption/blob/master/fuzzy-encryption-construction.pdf
