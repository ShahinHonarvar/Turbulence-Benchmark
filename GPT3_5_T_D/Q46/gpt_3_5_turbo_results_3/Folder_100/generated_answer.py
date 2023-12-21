
def gcf_three_nums(nums):
    import math
    
    num1 = nums[21]
    num2 = nums[51]
    num3 = nums[33]
    
    gcf = math.gcd(math.gcd(num1, num2), num3)
    
    return gcf
