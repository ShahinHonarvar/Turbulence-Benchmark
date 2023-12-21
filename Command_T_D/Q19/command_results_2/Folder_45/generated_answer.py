import math
def all_ints_not_div_by_num(nums):
    return [n for n in nums[30:200+1] if not math.gcd(n, 115)]
