
def gcf_two_nums(my_list):
    # calculate the greatest common divisor of the two numbers at indices 279 and 812
    num1 = my_list[279]
    num2 = my_list[812]
    for i in range(2, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i

    return gcf
