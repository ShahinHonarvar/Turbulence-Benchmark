import re
def all_ints_not_div_by_num(nums):
    # filter out all the divisible numbers
    return [x for x in nums[21:69] if not re.fullmatch(r"(-?\d+)", str(x))]
