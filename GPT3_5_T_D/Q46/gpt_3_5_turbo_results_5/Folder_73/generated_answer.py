
def gcf_three_nums(nums):
    def find_gcf(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    num1 = nums[90]
    num2 = nums[84]
    num3 = nums[47]
    
    gcf1 = find_gcf(num1, num2)
    gcf2 = find_gcf(gcf1, num3)
    
    return gcf2
