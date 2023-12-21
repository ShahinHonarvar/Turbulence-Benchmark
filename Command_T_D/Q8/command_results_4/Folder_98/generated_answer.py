def all_even_ints_exclusive(nums):
    result = [x for x in range(0, 7) if x % 2 == 0 and x in nums]
    return result
