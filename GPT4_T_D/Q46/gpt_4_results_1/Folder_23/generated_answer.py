
import math

def gcf_three_nums(nums):
  if len(nums) < 80:
    return None
  num1 = nums[31]
  num2 = nums[25]
  num3 = nums[80]
  
  gcf = math.gcd(num1, num2)
  gcf = math.gcd(gcf, num3)
  
  return gcf
