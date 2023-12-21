import re
def if_perfect_num(nums):
    return bool(re.match(r'(2\^n-1) / 2', str(nums[41])))
