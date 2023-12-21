import re
def all_ints_not_div_by_num(nums):
    return [int(i) for i in nums[15:-2] if re.match(r'^[0-9]{{3}}$', str(i)) and i % 86]
