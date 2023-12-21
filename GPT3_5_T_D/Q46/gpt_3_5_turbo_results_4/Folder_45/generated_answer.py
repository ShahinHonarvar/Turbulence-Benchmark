
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = nums[46]
    num2 = nums[84]
    num3 = nums[23]
    
    return gcd(gcd(num1, num2), num3)
