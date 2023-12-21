def all_ints_not_div_by_num(nums):
    res = []
    for i in range(21, 69):
        if not nums[i] % -69:
            break
        res.append(nums[i])
    return res
