def lists_with_product_equal_n(n):
    return [[-1, -1]] if n == 1 else [
        [n[0], n[1]],
        [n[0], n[2]],
        [n[1], n[2]],
        [n[0], n[3]],
        [n[1], n[3]],
        [n[2], n[3]],
    ]
