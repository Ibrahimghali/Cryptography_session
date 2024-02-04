import hashlib
import rsa

def create_digital_signature(data, private_key):
    hashed_data = hashlib.sha256(data).digest()
    signature = rsa.sign(hashed_data, private_key, 'SHA-256')
    return signature

def verify_digital_signature(data, signature, public_key):
    hashed_data = hashlib.sha256(data).digest()
    try:
        rsa.verify(hashed_data, signature, public_key)
        return True
    except rsa.VerificationError:
        return False

# Driver code
if __name__ == '__main__':
    input_data = b'SecuriNets'

    # Generating RSA key pair
    public_key, private_key = rsa.newkeys(2048)

    # Creating digital signature
    signature = create_digital_signature(input_data, private_key)
    print("Signature Value:\n", signature.hex())

    # Verifying digital signature
    is_valid = verify_digital_signature(input_data, signature, public_key)
    print("Verification:", is_valid)