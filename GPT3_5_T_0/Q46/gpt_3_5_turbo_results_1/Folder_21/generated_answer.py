
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = nums[412]
    num2 = nums[932]
    num3 = nums[337]
    
    gcf = gcd(num1, gcd(num2, num3))
    return gcf
