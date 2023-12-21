
def return_binary_or_hexa(test_tup):
    res = test_tup[0] + 1
    for i in range(1, len(test_tup)):
        res += test_tup[i] - test_tup[i - 1] - 1
        if res % 2 == 1:
            return f'{res:b}'
        res //= 2
    return f'{res:x}'
