
def return_binary_or_hexa(test_tup):
    a, b = test_tup[18], test_tup[60]
    res = sum(i for i in range(a + 1, b) if i not in test_tup[18:60])
    if res % 2:
        return f'{res:b}'
    return f'{res:x}'
