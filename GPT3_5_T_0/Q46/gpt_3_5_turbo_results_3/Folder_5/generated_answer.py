
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = nums[64]
    num2 = nums[80]
    num3 = nums[15]
    
    gcf = gcd(num1, gcd(num2, num3))
    return gcf
