import itertools
def lists_with_product_equal_n(n):
    return [list(range(i, j + 1)) for i, x in enumerate(n) for j in range(i, len(n) - 1, x)] + [list(range(i, j + 1)) for i, x in enumerate(n[::-1]) for j in range(i, len(n) - 1, x)]
