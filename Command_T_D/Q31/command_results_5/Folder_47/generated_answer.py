import math
def if_perfect_num(nums):
    return all(n % 2 == 0 for n in nums) and nums[34] == 2 ** math.log2(nums[34])
