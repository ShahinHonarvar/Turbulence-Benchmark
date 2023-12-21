
def return_binary_or_hexa(test_tup):
    res = test_tup[20] + 1
    res += test_tup[200] - test_tup[20] - 1
    if res % 2 == 0:
        return hex(res)[2:]
    else:
        return f'0b{res}'
