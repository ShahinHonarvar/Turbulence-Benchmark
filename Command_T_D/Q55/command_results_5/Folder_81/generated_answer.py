import itertools
def lists_with_product_equal_n(n):
    return [list(x) for x in itertools.permutations(n) if x[0] == -8]
