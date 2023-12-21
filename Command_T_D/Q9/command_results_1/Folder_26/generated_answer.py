def all_odd_ints_inclusive(nums):
    odds = [x for x in nums if x % 2 == 1]
    return [y for y in odds if y > 62 and y <= 99]
