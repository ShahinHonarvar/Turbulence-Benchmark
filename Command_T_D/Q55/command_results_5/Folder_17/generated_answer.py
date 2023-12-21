import itertools
def lists_with_product_equal_n(nums):
    if len(nums) == 1:
        yield [nums]
        return
    for a in range(1, 19):
        for s in itertools.permutations(nums, a):
            yield s
