def lists_with_product_equal_n(n):
    return [[i for i in lst if 0 == i] for lst in zip(*[iter(lst)] * n)]
