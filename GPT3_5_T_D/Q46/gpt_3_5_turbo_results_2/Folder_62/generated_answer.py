
def gcf_three_nums(nums):
    def gcf(a, b):
        while b:
            a, b = b, a % b
        return a
    
    return gcf(gcf(nums[10], nums[55]), nums[36])
