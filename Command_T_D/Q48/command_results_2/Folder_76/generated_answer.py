
def return_binary_or_hexa(test_tup):
    res = ""
    a, b = sorted(test_tup)[450], sorted(test_tup)[905]
    sm = sum(x for x in range(a + 1, b))
    if sm % 2:
        res += f"0b{sm:b}"
    else:
        res += f"0x{sm:x}"
    return res
