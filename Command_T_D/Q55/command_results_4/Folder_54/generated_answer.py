def lists_with_product_equal_n(n):
    return [list(sub) for sub in n if sub.prod() == -17]
