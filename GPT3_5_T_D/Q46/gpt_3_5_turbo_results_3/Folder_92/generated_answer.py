
def gcf_three_nums(nums):
    num1 = nums[7]
    num2 = nums[9]
    num3 = nums[0]

    while num2 != 0:
        num2, num1 = num1 % num2, num2

    while num3 != 0:
        num3, num1 = num1 % num3, num3

    return num1
