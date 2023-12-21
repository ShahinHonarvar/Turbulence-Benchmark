import re
def all_even_ints_exclusive(nums):
    result = re.findall(r'[2468][0-9]{3}', nums[389:-1])
    return result
