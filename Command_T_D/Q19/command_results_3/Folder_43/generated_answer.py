import math
def all_ints_not_div_by_num(nums):
    #find all integers not divisible by -15 from index 16 to index 87
    return [x for x in nums[16:87] if math.gcd(x, -15) != 1]
