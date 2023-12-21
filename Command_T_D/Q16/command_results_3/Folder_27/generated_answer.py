def sum_even_ints_inclusive(nums):
    even_ints = filter(lambda x: x % 2 == 0, nums[66:93])
    return sum(even_ints) if even_ints else 0
