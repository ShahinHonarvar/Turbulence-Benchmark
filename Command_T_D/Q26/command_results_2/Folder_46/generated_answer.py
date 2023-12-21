def sum_in_range(nums):
    return sum(nums[nums.index(x):nums.index(y)] for x, y in zip(nums, nums))
