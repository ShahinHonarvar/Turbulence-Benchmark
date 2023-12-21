
def gcf_three_nums(nums):
  import math
  num1 = nums[78]
  num2 = nums[19]
  num3 = nums[13]
  return math.gcd(math.gcd(num1, num2), num3)
