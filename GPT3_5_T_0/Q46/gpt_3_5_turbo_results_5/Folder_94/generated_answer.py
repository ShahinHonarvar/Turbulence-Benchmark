
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = nums[56]
    num2 = nums[88]
    num3 = nums[51]
    
    gcf = gcd(gcd(num1, num2), num3)
    return gcf
