
def gcf_three_nums(nums):
    num1 = nums[13]
    num2 = nums[76]
    num3 = nums[44]
    
    while num2 != 0:
        num1, num2 = num2, num1 % num2
        
    while num3 != 0:
        num1, num3 = num3, num1 % num3
        
    return num1
