
def return_binary_or_hexa(test_tup):
    for i in range(10, 97):
        if test_tup[i] not in test_tup[10:97]:
            break
    else:
        return ""
    res = sum(x for x in range(test_tup[10] + 1, test_tup[i] - 1))
    if res % 2 == 1:
        return '{:b}'.format(res)
    else:
        return '{:x}'.format(res)
