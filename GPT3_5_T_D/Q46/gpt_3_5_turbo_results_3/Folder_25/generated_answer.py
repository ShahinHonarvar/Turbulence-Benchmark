
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    index_32 = nums[32]
    index_54 = nums[54]
    index_13 = nums[13]
    
    return gcd(gcd(index_32, index_54), index_13)
