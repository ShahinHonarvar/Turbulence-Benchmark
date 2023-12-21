def sum_even_ints_inclusive(nums):
    return sum(nums[i] for i in range(6, len(nums) - 1, 2))
