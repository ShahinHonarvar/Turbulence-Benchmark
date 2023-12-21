import re
def if_perfect_num(nums):
    return bool(re.match(r'(1+8+9)1', str(nums[4])))
