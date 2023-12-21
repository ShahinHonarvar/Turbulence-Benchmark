
def return_binary_or_hexa(test_tup):
    res = str(sum(range(test_tup[0] + 1, test_tup[7] - 1, 2)))
    if res:
        return res.zfill(len(res))
    else:
        return str(sum(range(test_tup[0] + 1, test_tup[7] - 1, 2)))
