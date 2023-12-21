def all_odd_ints_exclusive(nums):
    result = [x for x in range(0, len(nums) + 1, 2) if x in nums]
    return result
