
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = nums[90]
    num2 = nums[54]
    num3 = nums[96]
    
    gcf = gcd(gcd(num1, num2), num3)
    
    return gcf
