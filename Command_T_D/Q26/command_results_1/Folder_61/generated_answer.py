def sum_in_range(nums):
    return sum(nums[x:x + 2] for x in range(len(nums) - 1) if x >= 8 and x + 1 <= 9)
