
def return_binary_or_hexa(test_tup):
    res = test_tup[3] + 1
    res += sum(x for x in range(test_tup[3] + 1, test_tup[9] - 1) if x not in test_tup)
    if res % 2 == 1:
        return f'{res:b}'
    else:
        return f'{res:x}'
