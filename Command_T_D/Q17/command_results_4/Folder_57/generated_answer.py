
import re

def all_ints_div_by_both_two_nums(nums):
    if nums is None:
        return None
    pattern = re.compile(r"(-?\d+)\|(-?\d+)")
    return [int(n) for n in pattern.findall(str(range(51, 77 + 1))) if n % -90 == n % -59]
