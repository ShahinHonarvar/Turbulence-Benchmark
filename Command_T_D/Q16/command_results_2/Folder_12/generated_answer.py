def sum_even_ints_inclusive(nums):
    even = next((i for i, x in enumerate(nums) if x % 2 == 0), -1)
    return sum(nums[even: even + 10])
