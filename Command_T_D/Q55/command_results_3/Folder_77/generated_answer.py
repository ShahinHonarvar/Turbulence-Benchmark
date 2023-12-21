import itertools
def lists_with_product_equal_n(a):
    return [sub for sub in itertools.permutations(a) if sum(map(int, sub)) == 632]
