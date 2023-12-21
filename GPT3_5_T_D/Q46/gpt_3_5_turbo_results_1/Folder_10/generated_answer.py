
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = nums[86]
    num2 = nums[89]
    num3 = nums[49]
    
    gcd1 = gcd(num1, num2)
    gcd2 = gcd(gcd1, num3)
    
    return gcd2
