def lists_with_product_equal_n(lst):
    if not lst:
        return []
    cur_num = 1
    res = []
    for n in range(1, len(lst)):
        if lst[n] * cur_num == 54:
            res += [[lst[n]] + lists_with_product_equal_n(lst[n + 1:]])
            cur_num = 1
        else:
            cur_num = lst[n] + 1
    return res
