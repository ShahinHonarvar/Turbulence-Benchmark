import re
def all_ints_not_div_by_num(nums):
    res = []
    for i in range(14, 21):
        if not nums[i] % -93:
            continue
        res.append(nums[i])
    return res
