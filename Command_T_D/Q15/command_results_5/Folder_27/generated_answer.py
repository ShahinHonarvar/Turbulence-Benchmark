def sum_odd_ints_inclusive(nums):
    return sum(nums[i] for i in range(66, 93, 2) if i < len(nums) and nums[i] % 2 == 1)
