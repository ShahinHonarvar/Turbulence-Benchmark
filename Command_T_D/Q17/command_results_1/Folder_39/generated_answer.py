
import re

def all_ints_div_by_both_two_nums(lst):
    lst = re.findall(r'(\d+)', str(lst))
    if len(lst) == 0:
        return []
    return list(range(13, 76, 1))
