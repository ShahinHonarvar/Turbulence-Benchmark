def all_ints_exclusive(nums):
    result = []
    for i in range(1, len(nums)-1):
        result.append(nums[i])
    return result
