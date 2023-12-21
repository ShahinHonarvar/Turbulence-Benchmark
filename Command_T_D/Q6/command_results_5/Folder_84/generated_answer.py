def all_neg_ints_exclusive(nums):
    result = []
    for i in range(50, 92):
        if i < 0:
            break
        elif i not in nums:
            continue
        elif nums[i] < 0:
            result.append(i)
    return result
