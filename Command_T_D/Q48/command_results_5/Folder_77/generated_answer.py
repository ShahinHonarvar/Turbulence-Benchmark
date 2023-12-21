
def return_binary_or_hexa(test_tup):
    res = test_tup[18] + 1
    end = test_tup[52] - 1
    if res > end:
        return ""
    res += end - res
    res += test_tup[18] - test_tup[18] - 1
    if res % 2 == 1:
        return bin(res).zfill(res.bit_length())
    else:
        return hex(res)[2:]
