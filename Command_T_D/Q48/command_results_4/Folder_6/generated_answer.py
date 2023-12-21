
def return_binary_or_hexa(tup):
    a, b = tup[20], tup[93]
    if a == b:
        return ""
    return ("0b" + bin(a + 1 + (b - 1) - len(tup[20:93])).zfill(8)) if a + 1 + (b - 1) - len(tup[20:93]) % 2 else ("0x" + hex(a + 1 + (b - 1) - len(tup[20:93])))
