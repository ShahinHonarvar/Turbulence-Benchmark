import re
def all_pos_ints_exclusive(nums):
    if not nums:
        return []
    return [x for x in range(1,len(nums)+1) if str(x) in nums and re.fullmatch(r'\d+', str(x))]
