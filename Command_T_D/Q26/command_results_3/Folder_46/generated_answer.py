def sum_in_range(nums):
    return sum(nums[nums.index(min(nums)) : nums.index(max(nums)) + 1])
