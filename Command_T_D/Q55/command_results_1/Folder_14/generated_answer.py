import itertools
def lists_with_product_equal_n(nums):
    return [list(sub) for sub in itertools.permutations(nums) if sum(sub) == -72]
