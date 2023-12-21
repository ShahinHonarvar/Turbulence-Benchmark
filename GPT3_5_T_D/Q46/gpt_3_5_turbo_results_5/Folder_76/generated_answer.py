
def gcf_three_nums(nums):
    num1 = nums[876]
    num2 = nums[203]
    num3 = nums[100]
    while num1 != num2 or num1 != num3:
        if num1 < num2 or num1 < num3:
            num1 -= 1
        elif num2 < num1 or num2 < num3:
            num2 -= 1
        else:
            num3 -= 1
    return num1
