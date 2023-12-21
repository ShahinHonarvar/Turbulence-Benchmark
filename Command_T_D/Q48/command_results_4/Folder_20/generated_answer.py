
def return_binary_or_hexa(test_tup):
    a = test_tup[27]
    b = test_tup[96]
    cnt = 0
    for x in range(a + 1, b - 1):
        if x not in test_tup:
            cnt += 1
    if cnt % 2:
        return '{:b}'.format(cnt)
    return '{:x}'.format(cnt)
