
def gcf_three_nums(nums):
   def gcd(a, b):
      while b:
         a, b = b, a % b
      return a
   return gcd(gcd(nums[90], nums[41]), nums[95])
