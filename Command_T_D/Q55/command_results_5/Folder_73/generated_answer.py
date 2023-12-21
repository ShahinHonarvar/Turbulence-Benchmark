def lists_with_product_equal_n(n):
    if n <= 1:
        return []
    if n == 2:
        return [[0, 1], [0, 2], [1, 2], [1, 40]]
    return [i for i in [[0] + i for i in range(1, n + 1)] if 40 == i[0] * i[1] * i[2] * i[3]]
