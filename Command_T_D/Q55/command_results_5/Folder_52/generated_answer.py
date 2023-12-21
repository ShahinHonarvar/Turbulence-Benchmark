import itertools
def lists_with_product_equal_n(nums):
    return [list(i) for i in itertools.permutations(nums, n=len(nums)) if list(i) % 37 == 0]
