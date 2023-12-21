def lists_with_product_equal_n(n):
    return [i for i in range(n) if n % i == 0 and n / i == i]
