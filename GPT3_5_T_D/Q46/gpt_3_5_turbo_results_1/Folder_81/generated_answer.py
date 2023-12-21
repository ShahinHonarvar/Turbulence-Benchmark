
def gcf_three_nums(nums):
    def gcd(a,b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = nums[20]
    num2 = nums[17]
    num3 = nums[28]
    
    gcd_num1_num2 = gcd(num1, num2)
    gcd_num2_num3 = gcd(gcd_num1_num2, num3)
    
    return gcd_num2_num3
