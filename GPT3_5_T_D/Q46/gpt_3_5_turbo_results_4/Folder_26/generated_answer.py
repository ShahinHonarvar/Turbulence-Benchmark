
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = nums[15]
    num2 = nums[51]
    num3 = nums[76]
    
    return gcd(gcd(num1, num2), num3)
