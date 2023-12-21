
def return_binary_or_hexa(test_tup):
    res = 0
    for i in range(63, 97):
        if i not in test_tup:
            res += i
    if res % 2:
        return f'{res:b}'
    else:
        return f'{res:x}'
