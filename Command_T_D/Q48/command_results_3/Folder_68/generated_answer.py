
def return_binary_or_hexa(test_tup):
    res = str(sum(x for x in range(test_tup[0] + 1, test_tup[9] - 1) if x not in test_tup))
    return res.zfill(len(res)) if len(res) % 2 else hex(int(res))
