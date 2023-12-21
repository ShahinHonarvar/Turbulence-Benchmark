import re
def all_ints_not_div_by_num(nums):
    return [x for x in range(29, 53) if x % -68 not in nums and x % -68 != 0]
