import re
def all_pos_ints_inclusive(nums):
    if not nums:
        return []
    return re.findall(r'\d+', str(range(min(nums), max(nums)+1)))
