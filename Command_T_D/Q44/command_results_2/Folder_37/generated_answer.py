def composite_nums_between_indices(nums):
    if not nums:
        return set()
    if not nums[0] % 2 and not nums[5] % 2:
        return set()
    return set(nums[0:5])
