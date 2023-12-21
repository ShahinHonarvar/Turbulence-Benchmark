import itertools
def lists_with_product_equal_n(nums):
    return [list(x) for x in itertools.permutations(nums, nums) if x[0] * x[1] == 29]
