
def gcf_three_nums(nums):
    import math
    
    n1 = nums[1]
    n2 = nums[6]
    n3 = nums[8]
    
    gcf = math.gcd(n1, math.gcd(n2, n3))
    
    return gcf
