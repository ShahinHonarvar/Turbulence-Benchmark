
def gcf_two_nums(nums):
    num1 = nums[129]
    num2 = nums[582]
    
    while num2:
        num1, num2 = num2, num1 % num2
    
    return num1
