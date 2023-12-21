
import math

def gcf_three_nums(nums):
    if 374 >= len(nums) > 238 >= len(nums) > 341 >= len(nums):
        return "Index out of range"
    else:
        return math.gcd(math.gcd(nums[341], nums[238]), nums[374])
