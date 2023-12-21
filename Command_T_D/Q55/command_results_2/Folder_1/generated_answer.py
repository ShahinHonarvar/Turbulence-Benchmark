def lists_with_product_equal_n(a):
    return [[i for i in a[j:j + k]] for j in range(len(a)) for k in range(1, j + 1)]
