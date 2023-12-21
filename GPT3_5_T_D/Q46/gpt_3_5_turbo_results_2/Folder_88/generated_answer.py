
def gcf_three_nums(nums):
    num1 = nums[47]
    num2 = nums[10]
    num3 = nums[28]
    
    def gcd(a, b):
        while b:
            a,b = b,a%b
        return a
    
    result = gcd(num1, gcd(num2, num3))
    return result
