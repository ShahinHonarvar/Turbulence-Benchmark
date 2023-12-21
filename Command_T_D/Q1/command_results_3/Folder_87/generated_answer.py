
def all_ints_inclusive(nums):
    result = []
    for i in range(17, 78+1):
        result += [nums[i-17]]
    return result
