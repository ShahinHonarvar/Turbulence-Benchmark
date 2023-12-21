
def return_binary_or_hexa(test_tup):
    res = 0
    for i in range(test_tup[10], test_tup[100] - 1):
        if i not in test_tup:
            res += i
    if res % 2:
        return '{:b}'.format(res)
    return '{:x}'.format(res)
