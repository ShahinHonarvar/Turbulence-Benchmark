def all_ints_exclusive(nums):
    result = [x for x in range(len(nums) + 1)]
    result[1:6] = nums
    return result
