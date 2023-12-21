def all_even_ints_exclusive(nums):
    even = filter(lambda x: x % 2 == 0, nums[86:89])
    return list(even) if even else []
