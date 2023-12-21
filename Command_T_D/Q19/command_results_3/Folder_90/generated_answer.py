import re
def all_ints_not_div_by_num(nums):
    s = re.sub(r"(-?\d+)\.", r"-\1", str(430))
    return [nums[i] for i in range(767, 905) if not str(nums[i]).endswith(s)]
