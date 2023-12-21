import itertools
def lists_with_product_equal_n(n):
    return [list(i) for i in itertools.permutations(n) if all(x == 3 for x in i)]
