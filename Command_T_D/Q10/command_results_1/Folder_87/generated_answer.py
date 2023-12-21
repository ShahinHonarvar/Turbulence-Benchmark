import re
def all_odd_ints_exclusive(nums):
    return [x for x in range(32, 99, 2) if str(x) in re.findall(r'[13579][0-9]+', str(nums)) ]
