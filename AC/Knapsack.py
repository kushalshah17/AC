import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_superincreasing(sequence):
    return all(sequence[i] > sum(sequence[:i]) for i in range(1, len(sequence)))

def generate_key():
    message_binary = input("Enter the binary message: ")
    num_elements = int(input("Enter the number of elements in the private key: "))
    private_key = [int(input(f"Enter element {i + 1}: ")) for i in range(num_elements)]

    if not is_superincreasing(private_key):
        print("Error: Private key is not in superincreasing sequence.")
        return

    sum_private_key = sum(private_key)
    m = random.randint(sum_private_key + 1, 2 * sum_private_key)

    while True:
        n = random.randint(2, m - 1)
        if gcd(n, m) == 1:
            break

    public_key = [(private_key[i] * n) % m for i in range(len(private_key))]

    print("Sum of private key:", sum_private_key)
    print("Generated m:", m)
    print("Generated n:", n)
    print("Public key:", public_key)

    while len(message_binary) > len(public_key):
        public_key *= 2

    encryption = sum(int(message_binary[i]) * public_key[i] for i in range(len(message_binary))) 

    print("Encrypted message:", encryption)

generate_key()
