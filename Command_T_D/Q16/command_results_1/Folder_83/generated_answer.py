def sum_even_ints_inclusive(nums):
    return sum(nums[i] for i in range(90, 200) if not nums[i] % 2)
