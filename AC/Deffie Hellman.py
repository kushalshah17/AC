def prime_checker(p):
    if p < 1:
        return -1
    elif p > 1:
        if p == 2:
            return 1
        for i in range(2, p):
            if p % i == 0:
                return -1
        return 1

def primitive_check(g, p, L):
    for i in range(1, p):
        L.append(pow(g, i) % p)
    for i in range(1, p):
        if L.count(i) > 1:
            L.clear()
            return -1
    return 1

def main():
    l = []

    while True:
        P = int(input("Enter P (a prime number): "))
        if prime_checker(P) == -1:
            print("Number Is Not Prime, Please Enter Again!")
            continue
        break

    while True:
        G = int(input("Enter The Primitive Root: "))
        if primitive_check(G, P, l) == -1:
            print("Not A Primitive Root, Please Try Again!")
            continue
        break

    x1 = int(input("Enter The Private Key Of User 1: "))
    x2 = int(input("Enter The Private Key Of User 2: "))
    while True:
        if x1 >= P or x2 >= P:
            print(f"Private Key Should Be Less Than Prime No.")
            continue
        break

    y1, y2 = pow(G, x1) % P, pow(G, x2) % P

    k1, k2 = pow(y2, x1) % P, pow(y1, x2) % P

    print("Secret Key For User 1 Is:", k1)
    print("Secret Key For User 2 Is:", k2)

    if k1 == k2:
        print("Key Exchange Successful")
    else:
        print("Key Exchange Unsuccessful")

main()
