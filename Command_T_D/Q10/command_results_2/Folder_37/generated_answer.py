def all_odd_ints_exclusive(nums):
    return [x for x in range(1, len(nums)+1) if x % 2 == 1 and x in nums]
