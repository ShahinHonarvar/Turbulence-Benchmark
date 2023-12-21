
def gcf_three_nums(nums):
    num1 = nums[70]
    num2 = nums[98]
    num3 = nums[22]
    
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    
    while num3 != 0:
        num1, num3 = num3, num1 % num3
    
    return num1
