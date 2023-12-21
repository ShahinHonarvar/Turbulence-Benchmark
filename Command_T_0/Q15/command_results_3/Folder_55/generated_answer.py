def sum_odd_ints_inclusive(nums):
    return sum(nums[i] for i in range(0, len(nums)) if i % 2 == 1)
