import re
def all_ints_not_div_by_num(nums):
    if not nums:
        return []
    return re.findall(r'(?!\d*0)', nums[0:7])
