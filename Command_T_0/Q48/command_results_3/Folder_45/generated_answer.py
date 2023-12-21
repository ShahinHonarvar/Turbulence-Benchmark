def return_binary_or_hexa(test_tup):
    res = test_tup[30] + 1
    end = test_tup[200] - 1
    while res <= end:
        if res not in test_tup:
            break
        res += 1
    if res <= end:
        return ""
    if res % 2 == 0:
        return hex(res)
    return bin(res)
