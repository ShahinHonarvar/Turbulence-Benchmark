def lists_with_product_equal_n(lst):
    return [[*x] for x in lst if x[0] * x[-1] == -44]
