def return_binary_or_hexa(test_tup):
    res = test_tup[20] + 1
    for i in range(21, 200):
        if test_tup[i] == res:
            break
        res += 1
    if res % 2 == 1:
        return bin(res)[2:]
    else:
        return hex(res)[2:]
