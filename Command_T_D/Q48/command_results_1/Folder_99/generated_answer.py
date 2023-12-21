
def return_binary_or_hexa(test_tup):
    res = sum(x for x in range(test_tup[427] + 1, test_tup[669] - 1) if x not in test_tup)
    if res % 2 == 1:
        return bin(res).zfill(res.bit_length())
    else:
        return hex(res)
