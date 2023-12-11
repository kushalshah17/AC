def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return "Modular inverse does not exist"

def affine_transform(char, a, b):
    x = ord(char) - ord('a')
    return chr(((a * x + b) % 26) + ord('a'))

def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        result += affine_transform(char, a, b)
    return result

def affine_decrypt(cipher, a, b):
    result = ""
    a_inv = mod_inverse(a, 26)
    for char in cipher:
        result += affine_transform(char, a_inv, -b)
    return result

def get_user_input():
    choice = input("Enter 'E' for encryption or 'D' for decryption: ").upper()
    if choice not in ['E', 'D']:
        print("Invalid choice. Please enter 'E' or 'D'.")
        return get_user_input()

    text = input("Enter: ")
    a = int(input("Enter key 1 'a': "))
    b = int(input("Enter key 2 'b': "))
    
    if choice == 'E':
        result = affine_encrypt(text, a, b)
        print("Encrypted text:", result)
    elif choice == 'D':
        result = affine_decrypt(text, a, b)
        print("Decrypted text:", result)

get_user_input()
