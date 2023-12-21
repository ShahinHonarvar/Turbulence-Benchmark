def all_neg_ints_exclusive(nums):
    result = []
    for i in range(389, 749):
        if i in nums and i < 0:
            result.append(i)
    return result
