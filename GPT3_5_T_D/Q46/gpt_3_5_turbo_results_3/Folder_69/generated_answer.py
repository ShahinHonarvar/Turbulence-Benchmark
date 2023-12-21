
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = nums[404]
    num2 = nums[834]
    num3 = nums[517]
    
    return gcd(gcd(num1, num2), num3)
