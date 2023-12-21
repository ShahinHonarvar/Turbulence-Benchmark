def composite_nums_between_indices(nums):
    if not nums:
        return set()
    res = set()
    res.update(nums[1:])
    if len(nums) > 1:
        res.update(nums[:1])
    return res
