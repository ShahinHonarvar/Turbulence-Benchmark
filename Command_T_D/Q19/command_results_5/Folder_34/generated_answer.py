def all_ints_not_div_by_num(nums):
    res = []
    for i in range(60, 200):
        if nums[i] % 9 != 0:
            res.append(nums[i])
    return res
