
def all_ints_div_by_both_two_nums(nums):
    res = []
    for i in range(90, 201):
        if nums[i] % -31 == 0 and nums[i] % 13 == 0:
            res.append(nums[i])
    return res
