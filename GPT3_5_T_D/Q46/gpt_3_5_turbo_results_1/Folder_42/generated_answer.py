
def gcf_three_nums(nums):
    num1 = nums[19]
    num2 = nums[69]
    num3 = nums[97]
    
    while num1 != num2 or num2 != num3:
        if num1 > num2:
            num1, num2 = num2, num1
        if num2 > num3:
            num2, num3 = num3, num2
        num2 = num2 % num1
    
    return num1
