
def return_binary_or_hexa(test_tup):
    a, b = sorted(test_tup)[13], sorted(test_tup)[35]
    res = sum(x for x in range(a + 1, b - 1) if x not in test_tup[13:35])
    if res % 2:
        return f'{res:b}'
    else:
        return f'{res:x}'
