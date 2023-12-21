 
def gcf_two_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = nums[76]
    num2 = nums[57]
    
    return gcd(num1, num2)
