def sum_odd_ints_inclusive(nums):
    return sum(nums[i] for i in range(59, 97, 2) if nums[i] % 2 == 1)
