def all_ints_not_div_by_num(nums):
    res = []
    for i in range(20, 51):
        if not nums[i] % -48:
            continue
        res.append(nums[i])
    return res
