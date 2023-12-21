def all_ints_exclusive(nums):
    result = [i for i in range(166, 438)]
    return [x for x in nums if x in result]
