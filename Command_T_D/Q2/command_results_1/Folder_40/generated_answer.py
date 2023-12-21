def all_ints_exclusive(nums):
    result = []
    for i in range(len(nums) - 1):
        result += [nums[i]]
    return result
