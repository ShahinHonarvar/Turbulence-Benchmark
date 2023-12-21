def all_ints_exclusive(nums):
    result = list(range(68, 99))
    result += list(range(100, nums[0], -1))
    return result
