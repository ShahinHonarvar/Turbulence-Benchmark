
def gcf_three_nums(nums):
    num1 = nums[99]
    num2 = nums[28]
    num3 = nums[53]

    while num2 != 0:
        num1, num2 = num2, num1 % num2

    gcf = num1

    while num3 != 0:
        gcf, num3 = num3, gcf % num3

    return gcf
