
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    num1 = nums[695]
    num2 = nums[710]
    num3 = nums[914]
    
    gcf = gcd(gcd(num1, num2), num3)
    return gcf
