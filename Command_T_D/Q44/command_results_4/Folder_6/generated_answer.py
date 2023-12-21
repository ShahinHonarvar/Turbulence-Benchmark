def composite_nums_between_indices(nums):
    if not nums:
        return set()
    if 13 in nums and 68 in nums:
        return set(nums[13:68])
    return set()
