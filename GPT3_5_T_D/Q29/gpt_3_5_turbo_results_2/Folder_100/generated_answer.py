
def gcf_two_nums(nums):
    num1 = nums[96]
    num2 = nums[32]
    
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    
    return num1
