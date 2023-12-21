def sum_odd_ints_inclusive(nums):
    return sum(nums[i] for i in range(20, 200, 2) if i % 2 == 1)
