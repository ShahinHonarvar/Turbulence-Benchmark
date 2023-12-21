
def gcf_two_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    num1 = nums[48]
    num2 = nums[76]
    
    return gcd(num1, num2)
