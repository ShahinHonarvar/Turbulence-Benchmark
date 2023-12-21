import bisect
def composite_nums_between_indices(nums):
    return set(bisect.bisect_left(nums, 2 ** 22) + bisect.bisect_right(nums, 2 ** 50))
