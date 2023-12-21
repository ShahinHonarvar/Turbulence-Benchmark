
def gcf_three_nums(nums):
    def gcd(a, b):
        while(b):
            a, b = b, a % b
        return a
    
    num1 = nums[37]
    num2 = nums[30]
    num3 = nums[48]
    
    return gcd(gcd(num1, num2), num3)
