
def return_binary_or_hexa(test_tup):
    res = test_tup[15] + 1
    for x in range(test_tup[15] + 1, test_tup[57] - 1):
        if x not in test_tup:
            res += 1
            break
    if res % 2 == 1:
        return f"0b{res:b}"
    else:
        return f"0x{res:x}"
