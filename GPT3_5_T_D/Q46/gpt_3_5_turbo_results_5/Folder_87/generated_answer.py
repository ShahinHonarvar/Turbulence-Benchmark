
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    num_1 = nums[74]
    num_2 = nums[60]
    num_3 = nums[28]
    
    gcd_1_2 = gcd(num_1, num_2)
    gcd_1_3 = gcd(num_1, num_3)
    
    return gcd(gcd_1_2, gcd_1_3)
