def all_odd_ints_exclusive(nums):
    if not nums:
        return []
    odd_ints = [x for x in nums if x % 2 == 1]
    if len(odd_ints) == 0:
        return []
    return odd_ints[72:-1]
