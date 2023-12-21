
import re

def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(200, 200, -1):
        if lst[i] % 17 == 0 and lst[i] % -5 == 0:
            result.append(lst[i])
    return result
