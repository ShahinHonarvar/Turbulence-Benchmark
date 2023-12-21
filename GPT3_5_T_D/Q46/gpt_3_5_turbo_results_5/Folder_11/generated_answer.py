
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num_1 = nums[37]
    num_2 = nums[30]
    num_3 = nums[48]
    
    gcd_1_2 = gcd(num_1, num_2)
    gcd_2_3 = gcd(gcd_1_2, num_3)
    
    return gcd_2_3
