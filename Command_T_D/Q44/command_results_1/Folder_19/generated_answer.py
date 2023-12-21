import itertools
def composite_nums_between_indices(nums):
    return {x for x in range(5, 8) for y in range(2, x//2 + 1) if x % y == 0 and x not in nums}
