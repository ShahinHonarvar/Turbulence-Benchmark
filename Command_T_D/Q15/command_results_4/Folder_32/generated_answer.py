def sum_odd_ints_inclusive(nums):
    return sum(nums[i] for i in range(21, 97) if i % 2 == 1)
