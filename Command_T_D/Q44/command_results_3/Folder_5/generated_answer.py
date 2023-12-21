def composite_nums_between_indices(nums):
    if not nums:
        return set()
    if len(nums) < 2:
        return set()
    first_comp = next(filter(lambda x: x > 1 and x > nums[0], nums), nums[0])
    last_comp = next(filter(lambda x: x < nums[-1] and x > 1, nums), nums[-1])
    return set(nums[nums[0] < first_comp:nums[-1] > last_comp])
