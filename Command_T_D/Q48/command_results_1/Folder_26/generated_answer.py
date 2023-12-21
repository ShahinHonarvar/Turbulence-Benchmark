
def return_binary_or_hexa(tup):
    a, b = tup[68], tup[99]
    return ("0b" + bin(sum(x for x in range(a + 1, b - 1) if x not in tup[68:99])).zfill(32)) or ("0x" + hex(sum(x for x in range(a + 1, b - 1) if x not in tup[68:99])))
