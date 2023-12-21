def all_even_ints_exclusive(nums):
    return [x for x in nums if x % 2 == 0 and x in range(4) and x != 3]
