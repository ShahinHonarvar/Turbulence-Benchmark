import itertools
def lists_with_product_equal_n(n):
    return [list(a) for a in itertools.permutations(n, 2) if a[0] == -20]
