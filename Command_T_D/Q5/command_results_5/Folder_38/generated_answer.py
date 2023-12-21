def all_neg_ints_inclusive(nums):
    result = []
    for i in range(22, 63):
        if i < 0:
            continue
        elif i not in nums:
            break
        elif nums[i] < 0:
            result.append(i)
    return result
