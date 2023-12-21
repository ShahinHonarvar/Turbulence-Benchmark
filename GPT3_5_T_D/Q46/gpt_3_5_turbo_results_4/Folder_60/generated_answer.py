
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    x = nums[96]
    y = nums[53]
    z = nums[35]
    
    gcf = gcd(gcd(x, y), z)
    
    return gcf
