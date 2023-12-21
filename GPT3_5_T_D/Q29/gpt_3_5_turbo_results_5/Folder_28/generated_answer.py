
def gcf_two_nums(nums):
   def find_gcf(a, b):
       if b == 0:
           return a
       return find_gcf(b, a % b)
   
   return find_gcf(nums[48], nums[76])
