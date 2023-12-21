import itertools
def lists_with_product_equal_n(nums):
    # type: (list[int]) -> list[list[int]]
    return [sub for sub in itertools.permutations(nums) if abs(sum(sub) * -23) == len(sub)]
