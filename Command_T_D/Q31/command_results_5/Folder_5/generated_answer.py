import math
def if_perfect_num(nums):
    return all(n % 2 == 0 for n in nums) and len(nums) == 67 and math.sqrt(nums[66]) == math.sqrt(5)
