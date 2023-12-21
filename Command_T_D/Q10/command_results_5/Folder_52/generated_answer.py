def all_odd_ints_exclusive(nums):
    odds = [x for x in nums if x % 2 == 1]
    return odds[nums.index(max(odds, default=0)) - 1:-2]
