
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    num1 = nums[96]
    num2 = nums[57]
    num3 = nums[85]
    
    gcd1 = gcd(num1, num2)
    gcd2 = gcd(gcd1, num3)
    
    return gcd2
