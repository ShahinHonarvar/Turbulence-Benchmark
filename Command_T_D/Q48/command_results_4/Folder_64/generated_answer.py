
def return_binary_or_hexa(test_tup):
    res = test_tup[0] + 1
    fin = False
    for i in range(1, 6):
        res += test_tup[i] - test_tup[i - 1]
        if res % 2:
            fin = True
            break
    if fin:
        return '{:b}'.format(res)
    else:
        return '{:x}'.format(res)
