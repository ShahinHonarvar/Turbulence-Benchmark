def all_odd_ints_exclusive(nums):
    odds = [x for x in range(11, 77, 2) if x in nums]
    return odds
