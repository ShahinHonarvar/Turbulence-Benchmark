
def gcf_three_nums(nums):
    def gcf(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = nums[14]
    num2 = nums[21]
    num3 = nums[17]
    
    gcf_num1_num2 = gcf(num1, num2)
    gcf_three_nums = gcf(gcf_num1_num2, num3)
    
    return gcf_three_nums
