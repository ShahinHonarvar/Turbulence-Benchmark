def all_odd_ints_inclusive(nums):
    odds = list(range(26, 52, 2))
    return [i for i in nums if i in odds]
