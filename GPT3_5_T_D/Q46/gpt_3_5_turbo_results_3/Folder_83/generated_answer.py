
def gcf_three_nums(nums):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    num1 = nums[56]
    num2 = nums[54]
    num3 = nums[13]
    
    gcf = gcd(gcd(num1, num2), num3)
    
    return gcf
