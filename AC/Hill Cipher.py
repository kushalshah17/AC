def encrypt_hill_cipher(plaintext, key_matrix):
    plaintext = plaintext.replace(" ", "").upper()
    if len(plaintext) % 2 != 0:
        plaintext += "X"
    numeric_text = [ord(char) - ord('A') for char in plaintext]
    groups_of_2 = [numeric_text[i:i+2] for i in range(0, len(numeric_text), 2)]
    encrypted_groups = []
    for group in groups_of_2:
        result = [
            (key_matrix[0][0] * group[0] + key_matrix[0][1] * group[1]) % 26,
            (key_matrix[1][0] * group[0] + key_matrix[1][1] * group[1]) % 26
        ]
        encrypted_groups += result
    encrypted_text = "".join([chr(num + ord('A')) for num in encrypted_groups])
    return encrypted_text

def decrypt_hill_cipher(ciphertext, key_matrix):
    ciphertext = ciphertext.replace(" ", "").upper()
    numeric_text = [ord(char) - ord('A') for char in ciphertext]
    groups_of_2 = [numeric_text[i:i+2] for i in range(0, len(numeric_text), 2)]
    det = key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]
    det_inverse = None
    for i in range(26):
        if (det * i) % 26 == 1:
            det_inverse = i
            break
    inv_key_matrix = [
        [(key_matrix[1][1] * det_inverse) % 26, (-key_matrix[0][1] * det_inverse) % 26],
        [(-key_matrix[1][0] * det_inverse) % 26, (key_matrix[0][0] * det_inverse) % 26]
    ]
    decrypted_groups = []
    for group in groups_of_2:
        result = [
            (inv_key_matrix[0][0] * group[0] + inv_key_matrix[0][1] * group[1]) % 26,
            (inv_key_matrix[1][0] * group[0] + inv_key_matrix[1][1] * group[1]) % 26
        ]
        decrypted_groups += result
    decrypted_text = "".join([chr(num + ord('A')) for num in decrypted_groups])
    return decrypted_text

choice = input("Enter 'E' for encryption or 'D' for decryption: ").upper()

if choice not in ['E', 'D']:
    print("Invalid choice. Please enter 'E' or 'D'.")
else:
    text = input("Enter the text: ")
    key_matrix = [[2, 3], [3, 6]]

    if choice == 'E':
        result = encrypt_hill_cipher(text, key_matrix)
        print("Encrypted Text:", result)
    else:
        result = decrypt_hill_cipher(text, key_matrix)
        print("Decrypted Text:", result)
