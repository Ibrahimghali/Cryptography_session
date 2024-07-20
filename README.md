# Cryptography Algorithms

This repository contains implementations of various cryptography algorithms in Python. The implementations are part of a cryptography session taught by me.

## Algorithms

1. **Caesar Cipher**
   - **File:** `caesar_cipher.py`
   - **Description:** Implements the Caesar cipher encryption and decryption algorithm. It shifts each character in the plaintext by a fixed number of positions.

2. **Digital Signature**
   - **File:** `digital_signature.py`
   - **Description:** Provides functions to generate and verify digital signatures using the SHA-256 hash algorithm and the RSA encryption algorithm.

3. **Vernam Cipher**
   - **File:** `vernam_cipher.py`
   - **Description:** Implements the Vernam cipher encryption and decryption algorithm. It combines the plaintext with a random key using the XOR operation.

4. **Hash Function**
   - **File:** `hash_function.py`
   - **Description:** Implements a hash function using the SHA-256 algorithm. It generates a fixed-size hash value for input data of any size.

5. **RSA**
   - **File:** `rsa.py`
   - **Description:** Provides functions for generating RSA key pairs, encrypting and decrypting data using the RSA algorithm, and signing and verifying digital signatures.

## Usage

Each algorithm is implemented in a separate Python file. You can use the provided functions in your own code by importing the respective file.

For example, to use the Caesar cipher algorithm:

```python
from caesar_cipher import encrypt, decrypt

plaintext = "Hello, World!"
key = 3

ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted_text = decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text)
