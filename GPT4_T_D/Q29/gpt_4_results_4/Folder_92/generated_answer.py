
import math
def gcf_two_nums(list_nums):
    if len(list_nums)>=2:
        return math.gcd(list_nums[0], list_nums[1])
    else:
        return "The list should contain at least two elements."
