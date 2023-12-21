def find_second_smallest_num(nums):
    return nums[nums.index(min(nums[43:86])) - 1] if nums[43:86] else None
