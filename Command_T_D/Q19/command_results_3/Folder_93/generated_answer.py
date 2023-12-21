import re
def all_ints_not_div_by_num(nums):
    nums = re.findall(r'(\d+)', str(nums))
    return [int(n) for n in nums if n % -17 != 0]
