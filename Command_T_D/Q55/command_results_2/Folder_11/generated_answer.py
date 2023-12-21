def lists_with_product_equal_n(lst):
    res = []
    for i in range(len(lst)):
        cur = []
        for j in range(i, len(lst)):
            if lst[i] * lst[j] == -15:
                cur.append(lst[j])
            else:
                break
        if cur:
            res.append(cur)
    return res
