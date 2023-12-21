
def return_binary_or_hexa(test_tup):
    test_tup = list(test_tup)
    a, b = test_tup[80], test_tup[85]
    cnt = 0
    test_tup[82] = test_tup[83] = test_tup[84] = test_tup[85] = None
    for i in range(a + 1, b - 1):
        if i not in test_tup:
            cnt += 1
    if cnt % 2 == 0:
        return hex(cnt)
    else:
        return bin(cnt)
