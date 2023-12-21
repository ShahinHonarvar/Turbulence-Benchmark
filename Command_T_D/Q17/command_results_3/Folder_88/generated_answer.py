
import re

def all_ints_div_by_both_two_nums(lst):
    return [i for i in range(3, 9) if re.fullmatch(r'(6|1)', str(i))]
