
def gcf_two_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    a = nums[64]
    b = nums[80]
    
    return gcd(a, b)
