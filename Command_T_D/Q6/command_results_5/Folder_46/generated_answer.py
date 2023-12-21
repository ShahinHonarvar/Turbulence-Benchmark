def all_neg_ints_exclusive(nums):
    result = []
    for i in range(20, 43):
        if i < 0:
            break
        elif i in nums:
            result.append(i)
    return result
