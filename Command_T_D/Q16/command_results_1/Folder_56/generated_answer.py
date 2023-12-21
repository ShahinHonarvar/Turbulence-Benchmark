def sum_even_ints_inclusive(nums):
    return sum(nums[i] for i in range(0, len(nums)) if nums[i] % 2 == 0)
