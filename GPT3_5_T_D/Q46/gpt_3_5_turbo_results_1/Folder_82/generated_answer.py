
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num_1 = nums[67]
    num_2 = nums[84]
    num_3 = nums[13]
    
    gcf = gcd(num_1, gcd(num_2, num_3))
    return gcf
