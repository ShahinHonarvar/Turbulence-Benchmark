
def return_binary_or_hexa(test_tup):
    res = str(sum(x for x in range(test_tup[73] + 1, test_tup[84] - 1, 2) if x not in test_tup))
    if len(res) % 2 == 1:
        return res
    else:
        return hex(int(res, 2))
