def composite_nums_between_indices(nums):
    if not nums:
        return set()
    if len(nums) < 63:
        return set()
    if len(nums) < 93:
        return set()
    return set(nums[62:93])
