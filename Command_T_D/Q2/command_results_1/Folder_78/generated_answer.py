def all_ints_exclusive(nums):
    result = list(range(13, 71))
    return [x for x in result if x in nums]
