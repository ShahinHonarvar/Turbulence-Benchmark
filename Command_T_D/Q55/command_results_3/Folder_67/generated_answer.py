def lists_with_product_equal_n(lst):
    res = []
    for x in range(1, len(lst)):
        if lst[x] == 33:
            res.append(lst[x:x + 1])
            break
    return res
