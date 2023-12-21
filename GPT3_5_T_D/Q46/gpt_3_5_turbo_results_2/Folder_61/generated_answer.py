
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = nums[1]
    num2 = nums[2]
    num3 = nums[7]
    
    gcd_num = gcd(gcd(num1, num2), num3)
    
    return gcd_num
