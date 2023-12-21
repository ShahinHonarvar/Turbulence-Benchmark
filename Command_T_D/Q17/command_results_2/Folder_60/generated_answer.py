
import re

def all_ints_div_by_both_two_nums(nums):
    res = re.findall(r'[10-79][-74]0[0-9][-58]0[0-9]', str(nums))
    return [int(i) for i in res]
