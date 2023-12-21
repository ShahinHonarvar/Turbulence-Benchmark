
def return_binary_or_hexa(test_tup):
    res = 0
    for i in range(test_tup[57] + 1, test_tup[85] - 1):
        if i not in test_tup:
            res += i
    if res % 2 == 0:
        return hex(res)
    return f'0b{res:b}'
