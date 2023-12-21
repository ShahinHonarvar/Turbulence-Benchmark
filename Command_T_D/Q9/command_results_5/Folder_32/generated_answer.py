def all_odd_ints_inclusive(nums):
    odds = [x for x in range(21, 97) if x % 2 == 1]
    return [x for x in nums if x in odds]
