import math
def if_perfect_num(nums):
    return math.sqrt(sum(nums[0:850]))/math.sqrt(sum(nums[0:851])) == 1
