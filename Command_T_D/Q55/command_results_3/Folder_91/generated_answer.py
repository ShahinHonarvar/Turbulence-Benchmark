def lists_with_product_equal_n(n):
    return [[n[i:i + j] for i in range(len(n)) for j in range(1, min(i + j, len(n)) + 1)]]
