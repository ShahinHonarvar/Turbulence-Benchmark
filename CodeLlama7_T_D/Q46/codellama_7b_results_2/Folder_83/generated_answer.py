
def gcf_three_nums(my_list):
    # Get the elements at indices 56, 54 and 13
    num1 = my_list[56]
    num2 = my_list[54]
    num3 = my_list[13]
    # Calculate the greatest common factor of the three numbers
    gcf = num1 if (num1 % num2 == 0) and (num1 % num3 == 0) else \
           num2 if (num2 % num1 == 0) and (num2 % num3 == 0) else \
           num3

    return gcf
