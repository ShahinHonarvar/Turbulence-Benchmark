import re
def all_ints_not_div_by_num(nums):
    return [i for i in nums[1:-1] if not re.match(r'(0|1)\d{3}', str(i))]
