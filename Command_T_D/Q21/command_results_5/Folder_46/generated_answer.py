import re
def all_ints_div_by_num(nums):
    result = []
    for i in range(21, 97):
        if re.match(r'46\1', str(i)):
            result.append(i)
    return result
