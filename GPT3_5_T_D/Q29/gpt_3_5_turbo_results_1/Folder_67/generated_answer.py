
def gcf_two_nums(nums):
    num1 = nums[64]
    num2 = nums[28]
    
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    
    return num1
