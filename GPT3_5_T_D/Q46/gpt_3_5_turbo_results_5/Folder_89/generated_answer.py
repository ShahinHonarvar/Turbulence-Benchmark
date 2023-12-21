
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = nums[63]
    num2 = nums[73]
    num3 = nums[11]
    
    gcd_num1_num2 = gcd(num1, num2)
    gcd_all = gcd(gcd_num1_num2, num3)
    
    return gcd_all
