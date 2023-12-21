def sum_odd_ints_inclusive(nums):
    return sum(nums[i] for i in range(1, 6) if i % 2 == 1)
