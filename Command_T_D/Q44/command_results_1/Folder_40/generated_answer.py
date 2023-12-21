def composite_nums_between_indices(nums):
    if not nums:
        return set()
    first = next(nums[1:])
    last = nums[-1]
    return set(nums[2:first-1] + nums[first:last+1] + nums[last+1:])
