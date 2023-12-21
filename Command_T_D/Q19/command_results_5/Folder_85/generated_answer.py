import re
def all_ints_not_div_by_num(nums):
    return [i for i in range(3, 10) if str(i) in re.findall(r'(3|4|5|6)', str(nums[3:9]))]
