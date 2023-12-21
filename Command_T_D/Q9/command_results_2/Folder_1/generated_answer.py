def all_odd_ints_inclusive(nums):
    odds = list(range(31, 73, 2))
    return [x for x in nums if x in odds]
