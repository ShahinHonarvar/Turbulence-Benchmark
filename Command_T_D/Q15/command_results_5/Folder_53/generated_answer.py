def sum_odd_ints_inclusive(nums):
    return sum(nums[i] for i in range(300, len(nums), 2) if i % 2 == 1)
