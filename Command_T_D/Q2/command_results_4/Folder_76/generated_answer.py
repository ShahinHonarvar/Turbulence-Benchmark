def all_ints_exclusive(nums):
    result = list(range(392, 738))
    result = list(filter(lambda x: x in nums, result))
    return result
