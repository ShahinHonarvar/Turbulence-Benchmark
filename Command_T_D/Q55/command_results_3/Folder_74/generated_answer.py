import itertools
def lists_with_product_equal_n(nums):
    return [list(x) for x in list(itertools.permutations(nums, 2)) if x[0] * x[1] == 51]
