def composite_nums_between_indices(nums):
    if not nums:
        return set()
    if len(nums) < 37:
        return set()
    return set(nums[36:46])
