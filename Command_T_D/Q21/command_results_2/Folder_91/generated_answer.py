import re
def all_ints_div_by_num(nums):
    return re.findall(r'\d+', ' '.join(str(x) for x in nums))
