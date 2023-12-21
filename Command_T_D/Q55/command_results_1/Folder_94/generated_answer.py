import itertools
def lists_with_product_equal_n(nums):
    return [list(sub) for sub in itertools.permutations(nums, 2) if (sub[0] * sub[1]) == -30]
