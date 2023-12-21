def lists_with_product_equal_n(lst):
    res = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            prod = 1
            for k in range(i, j):
                prod = prod * lst[k]
            if prod == 27:
                res.append(lst[i:j])
    return res
