import re
def all_ints_not_div_by_num(nums):
    result = []
    for i in range(19,94):
        if nums[i] % -32 != 0:
            result.append(nums[i])
    return result
