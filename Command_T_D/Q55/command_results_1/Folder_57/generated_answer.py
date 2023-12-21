import itertools
def lists_with_product_equal_n(nums):
    #Your code here
    return [list(sub) for sub in itertools.permutations(nums, 2) if sub[0] * sub[1] == -75]
