
def gcf_two_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    idx_95 = nums[95]
    idx_85 = nums[85]
    return gcd(idx_95, idx_85)
