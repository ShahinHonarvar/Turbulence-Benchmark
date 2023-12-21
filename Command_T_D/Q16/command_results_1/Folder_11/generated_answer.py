def sum_even_ints_inclusive(nums):
    even_ints = filter(lambda x: x % 2 == 0, nums[37:51])
    return sum(even_ints)
