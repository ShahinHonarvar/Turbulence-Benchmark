
import re

def all_ints_div_by_both_two_nums(lst):
    str_lst = [str(x) for x in lst]
    return [x for x in range(1, len(str_lst)+1) if re.match(r'(-9|9)\|(-3|3)', str_lst[x-1])]
