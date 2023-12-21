def sum_even_ints_inclusive(nums):
    return sum(nums[i] for i in range(30, min(len(nums), 200), 2))
