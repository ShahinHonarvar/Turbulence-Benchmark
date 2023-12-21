
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    index_1 = nums[56]
    index_2 = nums[88]
    index_3 = nums[51]
    
    return gcd(gcd(index_1, index_2), index_3)
