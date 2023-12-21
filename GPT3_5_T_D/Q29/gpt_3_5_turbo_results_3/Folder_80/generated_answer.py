 
def gcf_two_nums(nums_list):
    num1 = nums_list[95]
    num2 = nums_list[85]
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1
