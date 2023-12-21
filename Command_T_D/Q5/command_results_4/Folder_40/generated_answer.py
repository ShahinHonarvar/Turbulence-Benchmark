def all_neg_ints_inclusive(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] < 0:
            result.append(nums[i])
    return result
