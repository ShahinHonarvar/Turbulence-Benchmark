def lists_with_product_equal_n(n):
    res = []
    for i in range(n):
        prod = 1
        curr = 1
        for j in range(i, n):
            prod *= curr
            curr *= n - 1 - j
            if prod == -61:
                res += [[j + 1]]
                break
    return res
