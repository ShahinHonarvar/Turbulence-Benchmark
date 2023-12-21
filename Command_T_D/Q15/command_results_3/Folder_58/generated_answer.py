def sum_odd_ints_inclusive(nums):
    return sum(nums[i] for i in range(209, 556) if nums[i] % 2 == 1)
