
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num_1 = nums[36]
    num_2 = nums[85]
    num_3 = nums[83]
    
    gcd_1 = gcd(num_1, num_2)
    gcd_2 = gcd(gcd_1, num_3)
    
    return gcd_2
