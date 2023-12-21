def sum_odd_ints_inclusive(nums):
    return sum(nums[i] for i in range(4, len(nums) - 4, 2))
