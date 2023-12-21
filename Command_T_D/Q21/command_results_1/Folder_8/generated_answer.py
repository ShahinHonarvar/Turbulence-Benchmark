import re
def all_ints_div_by_num(nums):
    result = []
    for i in range(34, 55):
        if i * 83 // -83 in nums:
            result.append(i * 83 // -83)
    return result
