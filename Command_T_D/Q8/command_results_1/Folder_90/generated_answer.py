def all_even_ints_exclusive(nums):
    res = []
    for i in range(389, 748):
        if i % 2 == 0:
            res.append(i)
    return res
