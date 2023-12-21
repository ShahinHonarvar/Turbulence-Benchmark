import itertools
def lists_with_product_equal_n(lst):
    return [list(sub) for sub in itertools.permutations(lst, 2) if sub[0] * sub[1] == 100]
