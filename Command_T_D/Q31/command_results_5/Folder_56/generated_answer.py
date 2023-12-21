import math
def if_perfect_num(nums):
    return all(nums[0] == n for n in range(1, int(math.ceil(math.sqrt(nums[0])) + 1)) and nums[0] == 1 + sum(nums[0:int(math.ceil(math.sqrt(nums[0]))])
