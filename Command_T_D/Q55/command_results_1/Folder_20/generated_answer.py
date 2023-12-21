def lists_with_product_equal_n(n):
    return [[y for y in n if y == 1] for x in n if x == 1 or x == -1]
