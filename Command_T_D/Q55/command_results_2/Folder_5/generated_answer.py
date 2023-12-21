import itertools
def lists_with_product_equal_n(A):
    return [x for x in itertools.permutations(A) if x.product() == -33]
