
def return_binary_or_hexa(test_tup):
    res = test_tup[35] + 1
    idx = test_tup.index(test_tup[64])
    if idx != -1:
        res += test_tup[idx + 1] - test_tup[idx]
    if res % 2 == 0:
        return hex(res)[2:]
    else:
        return f'0b{res:b}'
