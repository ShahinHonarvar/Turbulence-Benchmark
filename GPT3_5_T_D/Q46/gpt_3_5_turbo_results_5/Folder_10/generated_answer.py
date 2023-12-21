
def gcf_three_nums(nums):
    def find_gcf(a, b):
        while b:
            a, b = b, a % b
        return a
    
    index_1 = nums[86]
    index_2 = nums[89]
    index_3 = nums[49]
    
    gcf = find_gcf(find_gcf(index_1, index_2), index_3)
    
    return gcf
