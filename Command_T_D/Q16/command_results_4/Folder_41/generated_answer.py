def sum_even_ints_inclusive(nums):
    even = next(i for i in range(len(nums) - 6) if nums[i] % 2 == 0)
    return nums[even:even + 2] + nums[even + 1:6]
