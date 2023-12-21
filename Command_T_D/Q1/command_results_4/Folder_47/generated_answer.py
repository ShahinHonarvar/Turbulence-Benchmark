
def all_ints_inclusive(nums):
    result = [num for num in range(29, 93)]
    result += [num for num in nums[29:93]]
    return result
