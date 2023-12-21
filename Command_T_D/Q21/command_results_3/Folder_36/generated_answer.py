import re
def all_ints_div_by_num(nums):
    result = []
    for i in range(421, 489+1):
        x = nums[i]
        if x%885 == 0:
            result.append(x)
    return result
