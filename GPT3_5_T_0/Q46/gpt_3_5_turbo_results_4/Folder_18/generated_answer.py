
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = nums[637]
    num2 = nums[411]
    num3 = nums[757]
    
    gcf = gcd(num1, gcd(num2, num3))
    return gcf
