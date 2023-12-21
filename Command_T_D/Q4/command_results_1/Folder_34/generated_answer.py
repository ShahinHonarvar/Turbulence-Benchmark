import re
def all_pos_ints_exclusive(nums):
    result = re.findall(r'\d+', range(60, 200))
    return [int(i) for i in result if i in nums]
