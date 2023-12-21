
def gcf_two_nums(nums):
    num1 = nums[19]
    num2 = nums[94]
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num1
