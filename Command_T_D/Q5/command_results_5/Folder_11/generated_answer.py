def all_neg_ints_inclusive(nums):
    result = []
    for i in range(37, 52):
        if i not in nums or nums[i] < 0:
            break
        result.append(nums[i])
    return result
