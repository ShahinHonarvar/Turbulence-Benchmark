import re
def all_ints_not_div_by_num(nums):
    s = nums[38:52+1]
    m = re.findall(r'([0-9]+)(?:\d{2})', s)
    return [int(i) for i in m if int(i) % -41 != 0]
