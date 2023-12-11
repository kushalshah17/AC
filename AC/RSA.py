import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return "Modular inverse does not exist"

def generate_keypair(p, q):
    n = p * q
    t = (p - 1) * (q - 1)
    e = random.randrange(2, t)
    while gcd(e, t) != 1:
        e = random.randrange(2, t)
    d = mod_inverse(e, t)
    return ((n, e), (n, d))

def encrypt(message, public_key):
    n, e = public_key
    ciphertext = pow(message, e, n)
    return ciphertext

def decrypt(ciphertext, private_key):
    n, d = private_key
    message = pow(ciphertext, d, n)
    return message

def main():
    plaintext = int(input("Enter the plaintext (integer): "))
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))
    public_key, private_key = generate_keypair(p, q)
    encrypted_message = encrypt(plaintext, public_key)
    decrypted_message = decrypt(encrypted_message, private_key)
    print("\nPublic Key (n, e):", public_key)
    print("Private Key (n, d):", private_key)
    print("\nPlaintext:", plaintext)
    print("Encrypted Message:", encrypted_message)
    print("Decrypted Message:", decrypted_message)

main()
