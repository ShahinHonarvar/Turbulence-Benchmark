def all_neg_ints_exclusive(nums):
    result = []
    for i in range(56, 92):
        if i not in nums:
            break
        elif nums[i] < 0:
            result.append(i)
    return result
