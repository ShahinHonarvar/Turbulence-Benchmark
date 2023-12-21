def all_odd_ints_exclusive(nums):
    result = [x for x in nums if x % 2 == 1]
    return result[:-1] if result else []
