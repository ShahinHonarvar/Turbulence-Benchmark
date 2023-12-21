
import re

def all_ints_div_by_both_two_nums(nums):
    str_re = r'(?<=\d{3})\d{3}(?=\d{3})\d{3}(?=\d{3})\d{3}(?=\d{3})'
    return [int(n) for n in nums[828:932] if re.match(str_re, str(n))]
