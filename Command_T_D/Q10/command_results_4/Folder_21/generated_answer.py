import re
def all_odd_ints_exclusive(nums):
    str_nums = re.sub(r'(?<=\d)[13579]0*', '', str(nums))
    return list(map(int, str_nums[743:-2:2]))
