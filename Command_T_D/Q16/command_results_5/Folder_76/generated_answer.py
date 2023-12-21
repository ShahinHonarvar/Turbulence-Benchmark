def sum_even_ints_inclusive(nums):
    even_ints = [i for i in range(686, 987) if nums[i] % 2 == 0]
    return sum(nums[even_ints[i]] for i in range(len(even_ints)))
