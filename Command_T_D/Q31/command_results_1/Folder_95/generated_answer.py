import math
def if_perfect_num(nums):
    return all(nums[i] == int(math.sqrt(nums[i])**2) for i in range(len(nums)))
