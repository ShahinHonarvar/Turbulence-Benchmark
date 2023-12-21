
def gcf_three_nums(nums):
    if len(nums) < 94:
        return None
    num_1 = nums[59]
    num_2 = nums[93]
    num_3 = nums[84]
    
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    gcf_1_2 = gcd(num_1, num_2)
    return gcd(gcf_1_2, num_3)
