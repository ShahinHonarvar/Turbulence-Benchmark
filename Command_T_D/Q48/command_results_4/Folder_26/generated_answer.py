
def return_binary_or_hexa(test_tup):
    a, b = test_tup[68], test_tup[99]
    sm = sum(test_tup[a + 1:b])
    return ("" if sm % 2 else "0b" + bin(sm).zfill(32).decode()) if sm else "0x" + hex(sm).zfill(32).decode()
