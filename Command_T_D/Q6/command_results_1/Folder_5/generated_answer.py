import re
def all_neg_ints_exclusive(nums):
    return re.findall(r"(-?\d+)$", str(nums)[2:-2])
