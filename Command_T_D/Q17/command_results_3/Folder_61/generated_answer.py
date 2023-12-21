
def all_ints_div_by_both_two_nums(nums):
    res = []
    for i in range(len(nums)):
        if nums[i] % -5 == 0 and nums[i] % -6 == 0:
            res.append(nums[i])
    return res
