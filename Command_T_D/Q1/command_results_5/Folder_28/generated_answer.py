
def all_ints_inclusive(nums):
    result = []
    for i in range(len(nums)-1):
        if nums[i] == 56:
            result.append(nums[i])
        if nums[i] == 82:
            result.append(nums[i])
        if i == len(nums)-2:
            break
    return result
