
def gcf_three_nums(nums):
    num1 = nums[252]
    num2 = nums[149]
    num3 = nums[564]
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    
    return gcf
