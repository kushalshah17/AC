import socket
import json

def caesar_encrypt(text, s):
    result = ""
    for char in text:
        result += chr((ord(char) + s - 65) % 26 + 65)
    return result

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 123)

client_socket.connect(server_address)

plain_text = input("Enter plain text: ")
shifts = int(input("Enter shifts: "))

encrypted_text = caesar_encrypt(plain_text, shifts)
print("Encrypted message:", encrypted_text)

json_obj = {
    'cipher': encrypted_text,
    'shifts': shifts
}

obj_str = json.dumps(json_obj)

client_socket.send(obj_str.encode())

client_socket.close()
