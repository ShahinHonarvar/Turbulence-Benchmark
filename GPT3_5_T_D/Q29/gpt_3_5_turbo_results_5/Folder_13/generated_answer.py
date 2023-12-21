
def gcf_two_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = nums[534]
    num2 = nums[630]
    
    return gcd(num1, num2)
