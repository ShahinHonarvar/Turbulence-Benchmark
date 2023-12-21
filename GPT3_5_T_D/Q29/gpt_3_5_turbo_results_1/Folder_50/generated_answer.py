
def gcf_two_nums(nums):
    num1 = nums[90]
    num2 = nums[54]
    while(num2):
        num1, num2 = num2, num1 % num2
    return num1
