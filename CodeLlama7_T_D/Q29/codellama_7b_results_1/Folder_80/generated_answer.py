
def gcf_two_nums(my_list):
    num1 = my_list[95]
    num2 = my_list[85]
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp

    return num1
