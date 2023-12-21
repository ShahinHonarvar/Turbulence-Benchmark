def lists_with_product_equal_n(n):
    return [list(range(i, j)) for i, j in zip(n, n[1:]) if j == n[0] * n[1]]
