import math
import random

# Step 1: Choose two small prime numbers
p, q = 101, 103

# Step 2: Compute n and Euler's Totient (phi)
n = p * q
phi = (p - 1) * (q - 1)

# Step 3: Choose a public key 'e' (must be coprime with phi)
e = 7


# Step 4: Find the private key 'd' such that (d * e) % phi = 1
def find_private_key(e, phi):
    d = 1
    while (d * e) % phi != 1:
        d += 1
    return d


d = find_private_key(e, phi)  # d is the private key


# Encryption function (RSA)
def encrypt(message, e, n):
    return pow(message, e, n)


# Decryption function (RSA)
def decrypt(encrypted_message, d, n):
    return pow(encrypted_message, d, n)


# Hwang’s additional security link: hash of user info, message, and signer's secret
def hwang_security_link(user_id, message, signer_secret):
    return (user_id + message + signer_secret) % signer_secret


# Blinding the message with a random number 'r'
def blind_message(message, e, n):
    r = random.randint(2, n - 1)
    while math.gcd(r, n) != 1:  # Ensure r is coprime with n
        r = random.randint(2, n - 1)
    blinded_message = (message * pow(r, e, n)) % n
    return blinded_message, r


# Unblinding the signed message
def unblind_message(signed_blinded_message, r, n):
    r_inv = pow(r, -1, n)  # Modular inverse of r
    unblinded_message = (signed_blinded_message * r_inv) % n
    return unblinded_message


# User ID Validation
def validate_user_id(user_id):
    """Validate if the user ID is a number and falls within a valid range"""
    if not isinstance(user_id, int):
        raise ValueError("User ID must be an integer.")
    if user_id < 1000 or user_id > 9999:  # Restricting user ID to a 4-digit number
        raise ValueError("User ID must be between 1000 and 9999.")
    return True


# Main program for Hwang's Blind Signature Scheme
if __name__ == "__main__":
    # Input from the user (original message)
    message = input("Enter a message to blind and sign: ")

    # Input and validate the User ID
    try:
        user_id = int(
            input("Enter your user ID (as a 4-digit number between 1000 and 9999): ")
        )
        validate_user_id(user_id)  # Validate the User ID
    except ValueError as ve:
        print(f"Error: {ve}")
        exit()

    message_int = sum(
        ord(char) for char in message
    )  # Convert the message to an integer
    print(f"\nOriginal message as integer: {message_int}")

    # Simulate a signer's secret (could be any large random number)
    signer_secret = random.randint(1000, 9999)

    # Step 1: Hwang's security link - combine user ID, message, and signer secret
    secure_link_message = hwang_security_link(user_id, message_int, signer_secret)
    print(f"Message with security link: {secure_link_message}")

    # Step 2: Blinding the message
    blinded_message, r = blind_message(secure_link_message, e, n)
    print(f"Blinded message: {blinded_message}")

    # Step 3: Signer signs the blinded message with their private key
    signed_blinded_message = decrypt(blinded_message, d, n)  # Sign the blinded message
    print(f"Signed blinded message: {signed_blinded_message}")

    # Step 4: Unblind the signed message
    unblinded_signature = unblind_message(signed_blinded_message, r, n)
    print(f"Unblinded signature: {unblinded_signature}")

    # Step 5: Verify the signature using the public key
    verified_message = encrypt(unblinded_signature, e, n)  # Verify the signature
    if verified_message == secure_link_message:
        print("Signature is valid!")
    else:
        print("Signature is invalid!")
