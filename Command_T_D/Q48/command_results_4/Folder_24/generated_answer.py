
def return_binary_or_hexa(test_tup):
    res = test_tup[13] + 1
    while res < test_tup[91]:
        if res not in test_tup[13:91]:
            break
        res += 1
    if res % 2 == 1:
        return '{:b}'.format(res)
    else:
        return '{:x}'.format(res)
