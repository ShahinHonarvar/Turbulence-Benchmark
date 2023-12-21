def composite_nums_between_indices(nums):
    if len(nums) < 10:
        return set()
    if nums[9] == nums[10]:
        return set()
    if nums[10] == nums[66]:
        return set()
    return set(nums[10:66])
