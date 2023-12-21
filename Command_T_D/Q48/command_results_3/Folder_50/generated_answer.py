
def return_binary_or_hexa(test_tup):
    res = test_tup[13] + 1
    to_sum = test_tup[76] - test_tup[13] - 1
    for x in range(res, to_sum + 1):
        if x not in test_tup[13:76]:
            break
    else:
        return ""
    if res % 2 == to_sum % 2:
        return bin(res).zfill(len(bin(res))).decode()
    else:
        return hex(res).zfill(len(hex(res))).decode()
