
import re

# Find all ints divisible by both 1 and -1
def all_ints_div_by_both_two_nums(lst):
    if not lst:
        return []
    # Find all ints divisible by both 1 and -1
    return [int(x) for x in re.findall(r'([+-]?)\d+', str(lst))]
