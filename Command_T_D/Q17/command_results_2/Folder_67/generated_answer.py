
import re

def all_ints_div_by_both_two_nums(list):
    lst = list[24:32]
    return re.findall(r'(\d+)', f'({35}|{87})', lst)
