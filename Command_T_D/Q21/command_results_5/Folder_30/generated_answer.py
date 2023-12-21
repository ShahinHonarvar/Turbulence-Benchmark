import re
def all_ints_div_by_num(nums):
    return [n for n in range(59,79+1) if int(str(n))%82==0 and int(str(n)) in nums]
