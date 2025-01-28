#import scr.fuzzyvault # Import all classes from the scr package
import scr.polynomial as poly

if __name__ == "__main__":
    # Create a new instance of the FuzzyVault class
    #vault = scr.fuzzyvault.FuzzyVault()
    # Call the addSecret method to add a secret to the vault

    secret = "password 123 456 test"

    poly.generate_polynomial(secret)