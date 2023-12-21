def all_odd_ints_exclusive(nums):
    return [x for x in range(3, 8) if x % 2 == 1 and x in nums]
