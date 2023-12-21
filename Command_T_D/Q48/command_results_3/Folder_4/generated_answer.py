
def return_binary_or_hexa(test_tup):
    res = test_tup[49] + 1
    if res <= test_tup[74]:
        return ""
    res += test_tup[74] - test_tup[49] - 1
    if res % 2 == 0:
        return hex(res)
    return f"0b{bin(res)[2:]}".zfill(len(bin(res)) - 2)
