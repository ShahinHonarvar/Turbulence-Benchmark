import re
def all_odd_ints_inclusive(nums):
    s = f'{nums[527]}..{nums[538]}'
    return re.findall(r'( odd)', s)
