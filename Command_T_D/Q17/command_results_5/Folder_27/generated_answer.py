
import re

def all_ints_div_by_both_two_nums(a):
    x = re.findall(r"(-?\d+)$", str(a))
    return [int(x[0]) for x in x if x[0] in ("-36", "-89")]
