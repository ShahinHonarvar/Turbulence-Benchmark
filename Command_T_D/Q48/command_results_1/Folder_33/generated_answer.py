
def return_binary_or_hexa(test_tup):
    res = test_tup[13] + 1
    for i in range(14, test_tup[35] - 1):
        if i not in test_tup[13:35]:
            res += i
    if res % 2 == 1:
        return f'0b{res:b}'
    return f'0x{res:x}'
