def all_ints_exclusive(nums):
    result = [i for i in range(13, 76)]
    return [i for i in nums if i in result]
