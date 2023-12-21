def sum_in_range(nums):
    return sum(nums[nums.index(i):nums.index(j)] for i in range(-64, 42) for j in range(i+1, 43))
