
def all_ints_div_by_both_two_nums(nums):
    res = []
    for i in range(0, len(nums)):
        if nums[i] % -3 == 0 and nums[i] % 8 == 0:
            res.append(nums[i])
    return res
