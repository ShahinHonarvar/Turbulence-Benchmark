import bisect
def composite_nums_between_indices(nums):
    return {x for x in range(bisect.bisect_left(nums, 2), bisect.bisect_right(nums, 8)) if all(x % r == 0 for r in range(2, x//2 + 1))}
