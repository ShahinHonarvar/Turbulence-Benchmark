
def gcf_three_nums(nums):
    num1 = nums[4]
    num2 = nums[1]
    num3 = nums[7]
    
    while num2:
        num1, num2 = num2, num1 % num2
    
    while num3:
        num1, num3 = num3, num1 % num3
    
    return num1
