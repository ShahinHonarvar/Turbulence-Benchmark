
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = nums[33]
    num2 = nums[78]
    num3 = nums[93]
    
    gcf = gcd(gcd(num1, num2), num3)
    return gcf
