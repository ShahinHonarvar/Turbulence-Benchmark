
def all_ints_inclusive(nums):
    result = []
    for i in range(len(nums)):
        if i >= 200:
            break
        result.append(nums[i])
    return result
