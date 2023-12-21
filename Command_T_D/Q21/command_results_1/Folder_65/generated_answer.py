def all_ints_div_by_num(nums):
    res = []
    for i in range(14, 56):
        if nums[i] % -59 == 0:
            res.append(nums[i])
    return res
