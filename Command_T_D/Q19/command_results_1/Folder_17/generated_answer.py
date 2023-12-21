def all_ints_not_div_by_num(nums):
    res = []
    for i in range(39, 57):
        if not nums[i]%84:
            break
        else:
            res.append(nums[i])
    return res
