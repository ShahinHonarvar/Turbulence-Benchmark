def all_ints_exclusive(nums):
    result = [i for i in range(len(nums)-2, -2, -1) if isinstance(nums[i], int)]
    return result
