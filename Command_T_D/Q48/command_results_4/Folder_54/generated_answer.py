
def return_binary_or_hexa(test_tup):
    res = test_tup[35] + 1
    cnt = test_tup[35]
    for i in range(test_tup[35] + 1, test_tup[64]):
        if i not in test_tup:
            res += i
            cnt += 1
    if cnt % 2 == 0:
        return hex(res)
    else:
        return bin(res)
