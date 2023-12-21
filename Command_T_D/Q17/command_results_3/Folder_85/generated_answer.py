
import re

def all_ints_div_by_both_two_nums(nums):
    return [int(n) for n in re.findall(r"(-9|3)[1-8]", str(nums)) if n.isdigit()]
