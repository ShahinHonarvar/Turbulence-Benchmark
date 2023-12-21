
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of the two numbers at indices 279 and 812
    num1 = my_list[279]
    num2 = my_list[812]
    gcf = 1

    while (num1 != 0) & (num2 != 0):
        if num1 > num2:
            num1 = num1 % num2

        else:
            num2 = num2 % num1

    return gcf
