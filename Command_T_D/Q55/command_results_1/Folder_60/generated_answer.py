def lists_with_product_equal_n(n):
    return [[i for i in range(n)] for i in range(1, n + 1) if n % i == 0 and i * i == 49]
