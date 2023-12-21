def all_odd_ints_inclusive(nums):
    return [x for x in range(10, 67) if x % 2 == 1 and x in nums]
