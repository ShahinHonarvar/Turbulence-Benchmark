def return_binary_or_hexa(test_tup):
    res = test_tup[25] + 1
    while res < test_tup[80]:
        if res not in test_tup:
            break
        res += 1
    if res % 2 == 1:
        return bin(res).zfill(res.bit_length())
    else:
        return hex(res)[2:]
