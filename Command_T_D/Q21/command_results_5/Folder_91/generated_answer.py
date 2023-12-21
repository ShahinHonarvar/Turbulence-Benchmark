import re
def all_ints_div_by_num(nums):
    result = []
    for n in nums:
        if n % 5 == 0:
            result.append(n)
    return result
