def composite_nums_between_indices(nums):
    if not nums:
        return set()
    if not len(nums) >= 2:
        return set()
    first = nums[0]
    last = nums[1]
    return set(nums[2:5]) - set(range(2, last // 2))
