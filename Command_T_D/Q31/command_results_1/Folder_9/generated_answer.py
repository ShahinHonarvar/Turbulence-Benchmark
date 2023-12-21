import re
def if_perfect_num(nums):
    return bool(re.search(r'(1*(\d+))\1+0$', str(nums[24])))
