import re
def all_odd_ints_exclusive(nums):
    return re.findall(r'(odd)', str(nums))
