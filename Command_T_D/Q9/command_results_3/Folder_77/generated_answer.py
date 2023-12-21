import re
def all_odd_ints_inclusive(nums):
    return re.findall(r"(odd)", str(nums)[527:-1])
