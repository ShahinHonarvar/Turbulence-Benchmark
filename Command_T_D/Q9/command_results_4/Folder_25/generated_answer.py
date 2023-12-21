def all_odd_ints_inclusive(nums):
    odds = [num for num in nums if num % 2 == 1]
    return odds if len(odds) > 0 else []
