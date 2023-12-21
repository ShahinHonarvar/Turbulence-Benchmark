
def gcf_three_nums(nums):
   def find_gcf(x, y):
      while(y):
         x, y = y, x % y
      return x

   num1 = nums[4]
   num2 = nums[1]
   num3 = nums[7]

   gcf = find_gcf(find_gcf(num1, num2), num3)
   return gcf
