
def gcf_three_nums(my_list):
    num1 = my_list[66]
    num2 = my_list[56]
    num3 = my_list[92]
    gcf = num1 if num1 % num2 == 0 and num1 % num3 == 0 else \
num2 if num2 % num1 == 0 and num2 % num3 == 0 else \
num3 if num3 % num1 == 0 and num3 % num2 == 0 else 1
    return gcf
