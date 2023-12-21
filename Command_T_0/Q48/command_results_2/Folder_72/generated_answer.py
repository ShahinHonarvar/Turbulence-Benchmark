def return_binary_or_hexa(test_tup):
    res = test_tup[13] + 1
    end = test_tup[70] - 1
    if res <= end:
        return ""
    res += end - res
    if res % 2 == 0:
        return hex(res)
    return bin(res)
