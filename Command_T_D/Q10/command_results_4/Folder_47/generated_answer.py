def all_odd_ints_exclusive(nums):
    odds = list(filter(lambda x: x & 1, nums[64:80:2]))
    return odds
