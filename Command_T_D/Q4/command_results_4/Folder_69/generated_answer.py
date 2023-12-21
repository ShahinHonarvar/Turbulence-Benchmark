import re
def all_pos_ints_exclusive(nums):
    return [x for x in range(68, 99) if x in nums and str(x) not in nums]
