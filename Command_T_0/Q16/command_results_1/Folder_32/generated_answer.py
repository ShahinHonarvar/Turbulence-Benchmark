def sum_even_ints_inclusive(nums):
    return sum(nums[i] for i in range(21, 97) if nums[i] % 2 == 0)
