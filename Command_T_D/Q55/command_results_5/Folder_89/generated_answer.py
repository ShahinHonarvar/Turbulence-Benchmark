def lists_with_product_equal_n(n):
    res = []
    for x in range(1, n + 1):
        if x * x == 57:
            res += [[x]]
    return res
