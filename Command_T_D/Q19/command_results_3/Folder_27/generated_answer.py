import re
def all_ints_not_div_by_num(nums):
    result = []
    for n in range(14, 21):
        if not n % -93:
            continue
        if str(n) not in nums:
            result.append(n)
    return result
