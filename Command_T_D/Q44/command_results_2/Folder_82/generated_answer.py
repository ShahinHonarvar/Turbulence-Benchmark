def composite_nums_between_indices(nums):
    if not nums:
        return set()
    if not (len(nums) > 30):
        return set()
    return set(nums[30:]) & set(nums[0:30])
