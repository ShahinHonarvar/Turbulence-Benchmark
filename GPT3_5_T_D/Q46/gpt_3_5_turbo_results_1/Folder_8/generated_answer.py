
def gcf_three_nums(nums):
    num1 = nums[99]
    num2 = nums[28]
    num3 = nums[53]

    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp

    while num3 != 0:
        temp = num3
        num3 = num1 % num3
        num1 = temp

    return num1
