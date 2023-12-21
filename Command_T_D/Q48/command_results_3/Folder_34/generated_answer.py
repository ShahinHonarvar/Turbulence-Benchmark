
def return_binary_or_hexa(test_tup):
    res = test_tup[60] + 1
    while res <= test_tup[200]:
        if res not in test_tup:
            break
        res += 1
    if res % 2 == 1:
        return f"0b{res:b}"
    else:
        return f"0x{res:x}"
