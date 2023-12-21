def sum_even_ints_inclusive(nums):
    even = next((i for i in range(14, 65) if nums[i] % 2 == 0), 0)
    return sum(nums[even:even + 33])
