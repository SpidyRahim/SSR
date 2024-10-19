import math

# Step 1: Choose two small prime numbers
p, q = 101, 103

# Step 2: Compute n and Euler's Totient (phi)
n = p * q  # n = 11 * 13 = 143
phi = (p - 1) * (q - 1)  # phi = (11-1) * (13-1) = 120

# Step 3: Choose a public key 'e' (must be coprime with phi)
e = 7  # A small prime number, and gcd(e, phi) = 1, so it's valid

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


# Step 5: Convert characters to numbers (using ASCII), then encrypt and decrypt
def encoder(message):
    return [encrypt(ord(char), e, n) for char in message]


def decoder(encoded_message):
    return "".join(chr(decrypt(num, d, n)) for num in encoded_message)


# Main program
if __name__ == "__main__":
    # Input from the user
    message = input("Enter the message you want to encrypt: ")

    # Encrypt the message
    encrypted_message = encoder(message)
    print("\nEncrypted message:", encrypted_message)

    # Decrypt the message
    decrypted_message = decoder(encrypted_message)
    print("\nDecrypted message:", decrypted_message)
