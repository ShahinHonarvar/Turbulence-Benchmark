
def return_binary_or_hexa(test_tup):
    res = test_tup[18] + 1
    idx = test_tup.index(test_tup[18])
    res += test_tup[idx:52]
    idx = test_tup.index(test_tup[52])
    res += test_tup[idx + 1 :]
    if res % 2:
        return '{:b}'.format(res)
    return '{:x}'.format(res)
