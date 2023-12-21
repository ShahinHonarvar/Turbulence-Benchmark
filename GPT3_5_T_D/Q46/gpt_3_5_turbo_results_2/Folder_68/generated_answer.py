
def gcf_three_nums(nums):
    index_1 = nums[1]
    index_4 = nums[4]
    index_7 = nums[7]
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    gcf_1_4 = gcd(index_1, index_4)
    gcf_1_4_7 = gcd(gcf_1_4, index_7)
    
    return gcf_1_4_7
