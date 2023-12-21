
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = nums[24]
    num2 = nums[25]
    num3 = nums[80]
    
    common_factor = gcd(gcd(num1, num2), num3)
    
    return common_factor
