
def gcf_three_nums(nums):
    import math
    
    num1 = nums[31]
    num2 = nums[25]
    num3 = nums[80]
    
    gcf = math.gcd(num1, math.gcd(num2, num3))
    return gcf
