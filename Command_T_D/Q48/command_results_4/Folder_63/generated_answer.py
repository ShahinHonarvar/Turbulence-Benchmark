
def return_binary_or_hexa(test_tup):
    res = test_tup[81] + 1
    if res > test_tup[86]:
        return ''
    res_set = set(test_tup)
    if res_set.issubset(list(range(res, test_tup[86] - 1, -1))):
        return ''
    res_set.update(list(range(res, test_tup[86] - 1, -1)))
    res_set.discard(res)
    if len(res_set) % 2 == 0:
        return hex(sum(res_set))
    else:
        return bin(sum(res_set))
