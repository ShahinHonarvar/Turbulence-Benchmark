
def return_binary_or_hexa(tup):
    a, b = tup[48], tup[76]
    res = sum(x for x in range(a + 1, b) if x not in tup[48:76])
    return ("0b" + bin(res)[2:][::-1]).zfill(res.bit_length() + 1) if res % 2 else hex(res)[2:][::-1]
