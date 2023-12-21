import re
def all_neg_ints_exclusive(nums):
    str_nums = " ".join(str(num) for num in nums)
    return re.findall(r"-?(\d+)", str_nums)[3:-1]
