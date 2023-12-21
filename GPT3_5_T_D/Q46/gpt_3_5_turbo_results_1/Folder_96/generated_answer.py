
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    gcd_29_74 = gcd(nums[29], nums[74])
    gcd_49 = gcd(gcd_29_74, nums[49])
    
    return gcd_49
