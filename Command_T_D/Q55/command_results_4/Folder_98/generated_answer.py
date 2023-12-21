import itertools
def lists_with_product_equal_n(s):
    lst = [x for x in itertools.permutations(s) if x[0] == -1]
    return [list(y) for y in lst if len(y) <= len(s)]
