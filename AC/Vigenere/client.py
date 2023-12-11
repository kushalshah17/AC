import socket
import json

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 123)

client_socket.connect(server_address)

text = input("Enter plain text: ")
key = input("Enter key of the same length: ")

cipher = ""
idx = 0

for char in text:
    shift = int(key[idx]) - int('0')
    encrypted_char = chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
    cipher += encrypted_char
    idx += 1

print("Cipher:", cipher)

json_obj = {
    'cipher': cipher,
    'key': key
}

obj_str = json.dumps(json_obj)
client_socket.send(obj_str.encode())

client_socket.close()
