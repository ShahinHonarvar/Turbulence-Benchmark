def lists_with_product_equal_n(n):
    if n < 1:
        return []
    return [[*l] for l in range(1, n + 1) if l == l[0] * l[1]]
