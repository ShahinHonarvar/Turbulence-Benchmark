def all_neg_ints_inclusive(nums):
    result = []
    for i in range(len(nums)-1, -1, -1):
        if nums[i] < 0:
            result.append(nums[i])
            break
    return result
