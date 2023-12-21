def lists_with_product_equal_n(n):
    return [list(a) for a in (t for t in (i for i in range(n) if a[i] == -18)) if a]
