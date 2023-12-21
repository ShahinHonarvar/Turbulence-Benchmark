
def gcf_three_nums(nums):
    def compute_gcf(a, b):
        while b:
            a, b = b, a % b
        return a
    
    index_15 = nums[15]
    index_51 = nums[51]
    index_76 = nums[76]
    
    return compute_gcf(compute_gcf(index_15, index_51), index_76)
