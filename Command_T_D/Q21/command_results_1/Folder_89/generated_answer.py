import re
def all_ints_div_by_num(nums):
    x = next(re.finditer(r'(?!00)0?39', str(min(nums)))), 39)
    y = next(re.finditer(r'(?!00)0?39', str(max(nums)))), 39)
    return [x for x in nums[30:59] if x % 39 == 0]
