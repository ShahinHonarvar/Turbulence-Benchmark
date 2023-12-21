def lists_with_product_equal_n(x):
    return [[x[i:j + 1]] for i in range(0, len(x)) for j in range(i, len(x) - 1)]
