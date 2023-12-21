
def gcf_three_nums(nums):
    num1 = nums[74]
    num2 = nums[60]
    num3 = nums[28]
    
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    
    while num3 != 0:
        num1, num3 = num3, num1 % num3
    
    return num1
