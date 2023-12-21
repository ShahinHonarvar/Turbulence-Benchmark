def composite_nums_between_indices(nums):
    if 2 in nums and 2 not in nums[1:]:
        return set(range(2, len(nums) + 1))
    else:
        return set()
