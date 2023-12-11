def permute(text):
    p_order = [2, 1, 0, 3, 4]
    p_text = [text[i] for i in p_order]
    print("Permuted Text:", p_text)
    return p_text, p_order

def encrypt(text):
    p_text, p_order = permute(text)
    s = 5
    cipher = ""
    for char in p_text:
        e_char = chr((ord(char) + s - ord('A')) % 26 + ord('A'))
        cipher += e_char
    return cipher, p_order, s

def decrypt(cipher, p_order, s):
    decrypted_text = ""
    for char in cipher:
        d_char = chr((ord(char) - s - ord('A')) % 26 + ord('A'))
        decrypted_text += d_char
    o_text = ['' for _ in range(len(p_order))]
    idx = 0
    for i in p_order:
        o_text[i] = decrypted_text[idx]
        idx += 1
    plain_text = "".join(o_text)
    return plain_text

t = input("Enter plain text: ")
c, p_order, s = encrypt(t)
d = decrypt(c, p_order, s)
print("Encrypted text:", c)
print("Decrypted text:", d)
