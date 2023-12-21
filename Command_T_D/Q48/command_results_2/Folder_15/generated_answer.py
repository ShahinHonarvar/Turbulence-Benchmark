
def return_binary_or_hexa(test_tup):
    res = ""
    test_tup = sorted(test_tup)
    test_tup = test_tup[:4]
    for x in range(test_tup[0] + 1, test_tup[4], 1):
        if x not in test_tup:
            res += str(x)
            break
    if len(res) == 0:
        return ""
    elif len(res) % 2 == 1:
        return res.zfill(len(res))
    else:
        return hex(int(res))
