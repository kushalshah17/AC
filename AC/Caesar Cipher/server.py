import socket
import json

def caesar_decrypt(ciphertext, s):
    result = ""
    for char in ciphertext:
        result += chr((ord(char) - s - 65) % 26 + 65)
    return result

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 123)

server_socket.bind(server_address)

server_socket.listen(1)

print("Server is listening on {}:{}".format(*server_address))

client_socket, client_address = server_socket.accept()
print("Connection established.")

obj = client_socket.recv(1024).decode()

data = json.loads(obj)
encrypt_msg = data['cipher']
shifts = data['shifts']

print("Encrypted message received:", encrypt_msg)

text = caesar_decrypt(encrypt_msg, shifts)
print("After decryption:", text)

server_socket.close()
client_socket.close()
