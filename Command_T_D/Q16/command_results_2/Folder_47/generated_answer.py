def sum_even_ints_inclusive(nums):
    return sum(nums[i] for i in range(len(nums)) if i % 2 == 0 and i >= 37 and i <= 76)
