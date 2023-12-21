def all_pos_ints_exclusive(nums):
    res = []
    for i in range(389, 748):
        if i in nums:
            res.append(i)
    return res
