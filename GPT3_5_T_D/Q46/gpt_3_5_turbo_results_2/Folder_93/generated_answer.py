
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = nums[25]
    num2 = nums[76]
    num3 = nums[57]
    
    common_factor = gcd(num1, gcd(num2, num3))
    
    return common_factor
