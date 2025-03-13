# Cipher text to plain text mapping
substitutions = {
    "X": "T",
    "W": "H",
    "O": "E",  # "THE" pattern
    "F": "W",
    "Y": "A",
    "D": "C",  # "WATCHER" pattern
    "A": "R",
    "P": "S",
    "K": "E",
    "M": "N",
    "I": "D",
    "U": "O",
    "Q": "I",  # Adjusted for frequency and word fit
    "B": "L",
    "J": "D",
    "T": "M",
    "Z": "Y",
    "C": "G",
    "G": "U",
    "V": "F",
    "H": "P",
}


# Function to decrypt the text using the above mapping
def decrypt(text, mapping):
    return "".join(mapping.get(char, char) for char in text)


# Function to encrypt the text using the above mapping
def encrypt(text, mapping):
    reverse_mapping = {v: k for k, v in mapping.items()}
    return "".join(reverse_mapping.get(char, char) for char in text)


# Example usage of the encrypt function
plaintext = """THE WATCHER SENDS THEIR REGARDS
FOLLOW THE SIGNAL
THE TIME DRAWS NEAR
FINALTRANSMISSION HTML
"""
encrypted_text = encrypt(plaintext, substitutions)
print("\nPlaintext:")
print(plaintext)
print("\nEncrypted Message:")
print(encrypted_text)

# Decrypt the ciphertext
decrypted_text = decrypt(encrypted_text, substitutions)
# Print result
print("Ciphertext:")
print(encrypted_text)
print("\nDecrypted Message:")
print(decrypted_text)
