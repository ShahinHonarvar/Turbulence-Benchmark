def lists_with_product_equal_n(n):
    return [x for x in [[y] for y in range(n) if -1 == y * (y + 1)]]
