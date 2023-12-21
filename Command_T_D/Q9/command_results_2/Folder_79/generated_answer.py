def all_odd_ints_inclusive(nums):
    result = []
    for i in range(4, len(nums) - 3, 2):
        result.append(nums[i])
    return result
