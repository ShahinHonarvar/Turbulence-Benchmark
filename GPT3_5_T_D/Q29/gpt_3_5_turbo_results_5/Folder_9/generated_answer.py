
def gcf_two_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    num1 = nums[84]
    num2 = nums[63]
    
    return gcd(num1, num2)
