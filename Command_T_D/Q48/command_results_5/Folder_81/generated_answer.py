
def return_binary_or_hexa(test_tup):
    res = test_tup[10] + 1
    cnt = 0
    for i in range(11, test_tup[100] - 1):
        if i not in test_tup:
            res += 1
            cnt += 1
    if cnt % 2:
        return '{:b}'.format(res)
    else:
        return '{:x}'.format(res)
