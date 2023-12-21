
def gcf_three_nums(nums):
    def get_gcf(a, b):
        while(b):
            a, b = b, a % b
        return a
    
    num1 = nums[17]
    num2 = nums[88]
    num3 = nums[35]
    
    gcf1 = get_gcf(num1, num2)
    gcf2 = get_gcf(gcf1, num3)
    
    return gcf2
