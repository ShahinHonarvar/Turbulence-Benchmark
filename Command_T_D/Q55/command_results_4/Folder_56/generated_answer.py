import itertools
def lists_with_product_equal_n(nums):
    for p in itertools.permutations(nums, 2):
        if p[0] * p[1] == -65:
            yield [p[0]] + [p[1]] + [p[0] for _ in range(nums[0] - 1)] + [p[1] for _ in range(nums[1] - 1)]
            yield [p[1]] + [p[0]] + [p[1] for _ in range(nums[0] - 1)] + [p[0] for _ in range(nums[1] - 1)]
