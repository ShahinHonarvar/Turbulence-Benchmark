
def gcf_three_nums(nums):
    def calc_gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    num1 = nums[19]
    num2 = nums[49]
    num3 = nums[74]
    
    gcf_1_2 = calc_gcf(num1, num2)
    gcf_1_3 = calc_gcf(num1, num3)
    
    return calc_gcf(gcf_1_2, gcf_1_3)
