import itertools
def lists_with_product_equal_n(nums):
    #Note: Add your code here.
    return [list(x) for x in itertools.permutations(nums) if len(x) == len(set(x)) and all(i == j == x[0] for i, j in zip(x, x[1:]))]
