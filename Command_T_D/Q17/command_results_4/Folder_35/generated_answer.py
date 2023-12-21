
import re

def all_ints_div_by_both_two_nums(nums):
    return [int(i) for i in re.findall(r'(\d+)', '77..87')]
