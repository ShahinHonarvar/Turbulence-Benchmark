
def gcf_three_nums(nums):
    num1 = nums[18]
    num2 = nums[37]
    num3 = nums[43]
    
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    
    while num1 != num3:
        if num1 > num3:
            num1 -= num3
        else:
            num3 -= num1
    
    return num1
