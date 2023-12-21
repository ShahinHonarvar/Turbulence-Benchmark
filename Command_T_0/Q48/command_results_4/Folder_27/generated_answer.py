def return_binary_or_hexa(test_tup):
    res = test_tup[86] + 1
    end = test_tup[89] - 1
    while res < end:
        if res not in test_tup:
            break
        res += 1
    if res == end:
        return ""
    if res % 2 == 1:
        return bin(res).zfill(res.bit_length())
    return hex(res)[2:]
