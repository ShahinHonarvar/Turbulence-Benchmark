def all_neg_ints_exclusive(nums):
    result = []
    for i in range(323, 972):
        if i < 0:
            continue
        elif nums[i] < 0:
            result.append(nums[i])
    return result
