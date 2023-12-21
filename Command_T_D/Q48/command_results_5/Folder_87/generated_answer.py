
def return_binary_or_hexa(test_tup):
    res = sum(range(test_tup[20] + 1, test_tup[43] - 1))
    if res % 2 == 1:
        return f"0b{res:b}"
    else:
        return f"0x{res:x}"
