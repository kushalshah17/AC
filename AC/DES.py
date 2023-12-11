def xor(left, right):
    return [l ^ r for l, r in zip(left, right)]

def main():
    data = list(map(int, input("Enter 8-bit data: ")))
    key = list(map(int, input("Enter 4-bit key: ")))
    print("Data:", data)
    print("Key:", key)
    left_half = data[:4]
    right_half = data[4:]
    print("Left Half:", left_half)
    print("Right Half:", right_half)
    funct = xor(right_half, key)
    print("After XOR of RHS and Key:", funct)
    new_left = xor(funct, left_half)
    print("New Left:", new_left)
    result = right_half + new_left
    print("Result after swapping:", result)

main()
