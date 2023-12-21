
def gcf_two_nums(nums):
    def gcf(a, b):
        return a if b == 0 else gcf(b, a%b)
    
    if len(nums) < 752:
        return None
    return gcf(nums[372], nums[752])
