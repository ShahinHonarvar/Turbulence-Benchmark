def all_odd_ints_exclusive(nums):
    odds = [n for n in nums if n % 2 == 1]
    return [o for o in odds if 70 <= o < 98]
