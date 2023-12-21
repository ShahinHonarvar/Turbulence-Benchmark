def all_even_ints_exclusive(nums):
    even = nums[598::2]
    return even[:-1] if len(even) > 1 else even
