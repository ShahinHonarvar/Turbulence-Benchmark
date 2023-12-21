
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = nums[19]
    num2 = nums[94]
    num3 = nums[78]
    
    gcd_num1_num2 = gcd(num1, num2)
    gcd_result = gcd(gcd_num1_num2, num3)
    return gcd_result
