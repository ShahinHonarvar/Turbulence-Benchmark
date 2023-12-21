
def gcf_three_nums(nums):
    num1 = nums[74]
    num2 = nums[51]
    num3 = nums[27]
    
    while num1 != num2 or num1 != num3:
        if num1 > num2 or num1 > num3:
            num1 = num1 - min(num1 - num2, num1 - num3)
        else:
            num2 = num2 - min(num2 - num1, num2 - num3)
            
    return num1
