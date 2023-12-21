
import re

def all_ints_div_by_both_two_nums(nums):
    lst = list(range(40,200+1))
    if not nums:
        return []
    for i in range(40,200+1):
        x = str(lst[i])
        if re.search(r'21|71', x):
            yield lst[i]
    return
