
def gcf_three_nums(nums):
    idx_1, idx_2, idx_3 = 67, 84, 13
    num_1, num_2, num_3 = nums[idx_1], nums[idx_2], nums[idx_3]
    
    def gcd(a, b):
        while b:
            a , b = b , a % b
        return a
    
    return gcd(gcd(num_1, num_2), num_3)
