def lists_with_product_equal_n(n):
    res = []
    for i in range(1, n + 1):
        if n % i == 0:
            res += [[i] + [x for x in range(i, n, i)]]
    return res
