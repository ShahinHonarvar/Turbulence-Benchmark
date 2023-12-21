
def return_binary_or_hexa(test_tup):
    a, b = 27, 96
    res = 0
    for i in range(a + 1, b):
        if i not in test_tup:
            res += i
    if res % 2:
        return f'{res:b}'
    else:
        return f'{res:x}'
