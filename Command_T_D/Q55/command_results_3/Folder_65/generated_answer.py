def lists_with_product_equal_n(n):
    if n < 4:
        return []
    res = []
    p = 1
    for i in range(n):
        p *= i + 1
        if p == 46:
            res.append([i + 1])
            p //= i + 1
    return res
