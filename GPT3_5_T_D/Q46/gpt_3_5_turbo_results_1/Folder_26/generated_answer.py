
def gcf_three_nums(nums):
    def compute_gcf(a, b):
        while(b):
            a, b = b, a % b
        return a
    
    gcf = nums[15]
    gcf = compute_gcf(gcf, nums[51])
    gcf = compute_gcf(gcf, nums[76])
    return gcf
