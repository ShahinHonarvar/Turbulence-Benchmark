
def gcf_three_nums(nums):
    num1 = nums[9]
    num2 = nums[6]
    num3 = nums[2]

    while num2 != 0:
        num1, num2 = num2, num1 % num2

    while num1 != 0 and num3 != 0:
        num1, num3 = num3, num1 % num3

    return num1
