def sum_odd_ints_inclusive(nums):
    return sum(nums[i] for i in range(263, 747) if i % 2)
