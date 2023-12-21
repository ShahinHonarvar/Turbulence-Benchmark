def lists_with_product_equal_n(n):
    return [[n[i:i + j] for i in range(0, len(n) - 1)] for j in range(1, len(n) + 1)]
