import itertools
def lists_with_product_equal_n(n):
    return [x for x in itertools.permutations(n) if x[0] == x[-1] and x[0] == 537]
