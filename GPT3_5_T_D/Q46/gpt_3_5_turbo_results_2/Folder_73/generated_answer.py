
def gcf_three_nums(nums):
    import math
    
    num1 = nums[90]
    num2 = nums[84]
    num3 = nums[47]
    
    return math.gcd(math.gcd(num1, num2), num3)
