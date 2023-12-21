
def gcf_three_nums(nums):
    num1 = nums[40]
    num2 = nums[15]
    num3 = nums[99]
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    gcd_num1_num2 = gcd(num1, num2)
    gcf = gcd(gcd_num1_num2, num3)
    return gcf
