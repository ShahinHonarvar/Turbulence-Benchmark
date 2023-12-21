def all_ints_not_div_by_num(nums):
    res = []
    for i in range(21,70):
        if not i%69:
            break
        res.append(i)
    return res
