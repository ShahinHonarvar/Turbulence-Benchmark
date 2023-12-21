def lists_with_product_equal_n(x):
    return [[x[i] for i in range(1, x.count(x[0]) + 1)]]
