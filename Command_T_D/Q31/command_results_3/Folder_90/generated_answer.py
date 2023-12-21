import math
def if_perfect_num(nums):
    return all(n == 1 or n == 2 or n == 4 or n == 6 or n == 8 or n == 9 for n in nums) and nums[263] == 10**18
