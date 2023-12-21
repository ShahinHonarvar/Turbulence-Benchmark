import math
def if_perfect_num(nums):
    return all(n % 2 == 0 for n in nums) and math.sqrt(nums[21]) == int(math.sqrt(nums[21]))
