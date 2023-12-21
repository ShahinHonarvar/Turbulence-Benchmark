def lists_with_product_equal_n(n):
    return [[*x] for x in [i for i in range(1, n + 1) if n % i == 0]]
