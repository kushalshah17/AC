def shift(k):
    return k[1:] + k[:1]

def gen_round_key():
    key = input("Enter 12-bit key: ")
    print("Original Key (12-bit):", key)
    p_table = [4, 9, 7, 1, 0, 3, 5, 2]
    pd_key = ''.join(key[i] for i in range(len(key)) if i != 5 and i != 11)
    print("After Parity Drop:", pd_key)
    C = pd_key[:5]
    D = pd_key[5:]
    print("C (left):", C)
    print("D (right):", D)
    C_after_shift = shift(C)
    D_after_shift = shift(D)
    print("C after Left Shift:", C_after_shift)
    print("D after Left Shift:", D_after_shift)
    comb_halves = C_after_shift + D_after_shift
    print("Combined C+D after Left Shift:", comb_halves)
    round_key = ''.join(comb_halves[i] for i in p_table)
    print("Key after Permutation:", round_key)

gen_round_key()
