def all_neg_ints_exclusive(nums):
    result = []
    for i in range(1, len(nums)):
        if nums[i] < 0:
            result.append(nums[i])
            break
    return result
