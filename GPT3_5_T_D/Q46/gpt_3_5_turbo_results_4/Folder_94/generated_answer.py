
def gcf_three_nums(nums):
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    num1 = nums[56]
    num2 = nums[88]
    num3 = nums[51]
    
    gcf_1_2 = gcf(num1, num2)
    gcf_all = gcf(gcf_1_2, num3)
    
    return gcf_all
