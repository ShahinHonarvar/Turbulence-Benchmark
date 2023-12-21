import re
def all_ints_not_div_by_num(nums):
    for i in range(495, 826):
        if not nums[i] % -201:
            continue
        else:
            return [i]
    return []
