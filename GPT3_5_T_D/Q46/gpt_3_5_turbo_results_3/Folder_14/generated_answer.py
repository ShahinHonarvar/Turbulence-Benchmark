
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num_1 = nums[17]
    num_2 = nums[88]
    num_3 = nums[35]
    
    gcd_1_2 = gcd(num_1, num_2)
    gcf = gcd(gcd_1_2, num_3)
    
    return gcf
