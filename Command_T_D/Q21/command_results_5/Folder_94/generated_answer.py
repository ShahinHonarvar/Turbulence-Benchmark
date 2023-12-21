import re
def all_ints_div_by_num(nums):
    return re.findall(r"-?[0-9]{%d,%d}" % (18,93), nums)
