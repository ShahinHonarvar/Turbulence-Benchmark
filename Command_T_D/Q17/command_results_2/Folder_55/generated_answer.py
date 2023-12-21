
import re

def all_ints_div_by_both_two_nums(nums):
    if not nums:
        return []
    if len(nums) < 10:
        return []
    return re.findall(r'(\d{1,2})(\d{3})(\d{4})(\d{5})(\d{6})(\d{7})(\d{8})(\d{9})', nums)
