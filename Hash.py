# Simple Hash Algorithm with Fixed Output Length
def simple_fixed_length_hash(message, bit_size=32):
    hash_value = 0

    for char in message:
        # Ordinal value of the character (ASCII)
        char_value = ord(char)

        # Example: Shift hash value left by 5 bits, and add char_value
        hash_value = ((hash_value << 5) - hash_value) + char_value

        # Keep the hash value within a fixed size using bitwise AND (2^bit_size - 1)
        hash_value = hash_value & ((1 << bit_size) - 1)

    # Convert to hexadecimal and zero pad to ensure fixed output length
    return f"{hash_value:0{bit_size // 4}x}"  # Hexadecimal representation


# Main program
if __name__ == "__main__":
    message = input("Enter a message to hash: ")

    # Calculate the hash of the message with fixed 32-bit length
    hashed_message = simple_fixed_length_hash(message, bit_size=32)

    print(f"Hashed value (32-bit): {hashed_message}")
