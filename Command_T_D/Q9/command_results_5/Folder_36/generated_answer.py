import re
def all_odd_ints_inclusive(nums):
    return re.findall(r'( odd)?\d+', nums[246:750+1])
