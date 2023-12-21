def sum_in_range(nums):
    return sum(nums[nums.index(x):nums.index(x + 65)] for x in range(-23, 65))
