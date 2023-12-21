
def all_ints_inclusive(nums):
    result = []
    for i in range(4, len(nums)-1, 2):
        result.append(nums[i])
    return result
