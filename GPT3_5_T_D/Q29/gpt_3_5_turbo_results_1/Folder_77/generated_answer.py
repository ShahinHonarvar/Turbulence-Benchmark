
def gcf_two_nums(nums):
    num1 = nums[841]
    num2 = nums[804]
    
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    
    return num1
