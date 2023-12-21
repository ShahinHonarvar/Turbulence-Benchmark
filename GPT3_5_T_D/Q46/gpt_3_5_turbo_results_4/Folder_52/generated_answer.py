
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    num1 = nums[19]
    num2 = nums[49]
    num3 = nums[74]
    
    factor = gcd(num1, num2)
    gcf = gcd(factor, num3)
    
    return gcf
