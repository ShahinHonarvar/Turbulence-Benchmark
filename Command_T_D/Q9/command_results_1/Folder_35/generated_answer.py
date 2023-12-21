def all_odd_ints_inclusive(nums):
    odds = [i for i in range(30, 49) if i % 2 == 1]
    return [x for x in nums if x in odds]
