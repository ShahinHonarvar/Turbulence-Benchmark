def lists_with_product_equal_n(list1):
    return [list(x) for x in list1 if len(x) > 1 and x[0] * x[-1] == 990]
