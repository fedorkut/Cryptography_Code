# Import required libraries
from secretpy import Caesar
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from functools import reduce
import numpy as np

# Set the plaintext we want to encrypt
plaintext = u"this is a strict top secret message for intended recipients only"
print(f"\nGiven plaintext: {plaintext}")

# Initialize the required object for Caesar shift encryption
caesar_cipher = Caesar()

# Define the Caesar cipher key and alphabet
caesar_key = 5
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ')

# Encrypt using Caesar cipher
caesar_ciphertext = caesar_cipher.encrypt(plaintext, caesar_key, alphabet)
print(f"Encrypted Caesar shift ciphertext: {caesar_ciphertext}")

# Decrypt the Caesar ciphertext
caesar_plaintext = caesar_cipher.decrypt(caesar_ciphertext, caesar_key, alphabet)
print(f"Decrypted Caesar shift plaintext: {caesar_plaintext}\n")

# Generate a random 16-character AES key and initialization vector (IV)
aes_key = reduce(lambda a, b: a + b, [np.random.choice(alphabet) for i in range(16)])
print(f'AES secret key: {aes_key}')

aes_initialization_vector = reduce(lambda a, b: a + b, [np.random.choice(alphabet) for i in range(16)])
print(f"AES initialization vector: {aes_initialization_vector}")

# Set up the AES encryptor with the key and IV
sender_aes_cipher = Cipher(algorithms.AES(bytes(aes_key, 'utf-8')), modes.CBC(bytes(aes_initialization_vector, 'utf-8')))
aes_encryptor = sender_aes_cipher.encryptor()

# Apply PKCS7 padding to make the plaintext a multiple of the block size
padder = padding.PKCS7(algorithms.AES.block_size).padder()
padded_plaintext = padder.update(bytes(plaintext, 'utf-8')) + padder.finalize()

# Encrypt the padded plaintext
aes_ciphertext = aes_encryptor.update(padded_plaintext) + aes_encryptor.finalize()
print(f"Encrypted AES ciphertext: {aes_ciphertext}")

# Set up the AES decryptor with the same key and IV
receiver_aes_cipher = Cipher(algorithms.AES(bytes(aes_key, 'utf-8')), modes.CBC(bytes(aes_initialization_vector, 'utf-8')))
aes_decryptor = receiver_aes_cipher.decryptor()

# Decrypt the ciphertext
aes_plaintext_bytes = aes_decryptor.update(aes_ciphertext) + aes_decryptor.finalize()

# Remove padding after decryption to retrieve the original plaintext
unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
unpadded_plaintext_bytes = unpadder.update(aes_plaintext_bytes) + unpadder.finalize()
aes_plaintext = unpadded_plaintext_bytes.decode('utf-8')

print(f"Decrypted AES plaintext: {aes_plaintext}")
