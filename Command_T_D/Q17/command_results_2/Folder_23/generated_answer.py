
import re

def all_ints_div_by_both_two_nums(lst):
    return [x for x in range(69, 97) if re.match("-90|-67$", str(x)) and x in lst]
