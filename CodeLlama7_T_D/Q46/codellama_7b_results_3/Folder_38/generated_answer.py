
def gcf_three_nums(my_list):
    # Calculate the greatest common factor (GCF) of three numbers in a list using Euclid's algorithm
    num1 = my_list[14]
    num2 = my_list[21]
    num3 = my_list[17]
    if num1 == 0:
        return num2

    elif num2 == 0:
        return num1

    else:

        while num1 != 0 and num2 != 0:
            if num1 > num2:
                num1 = num1 % num2

            else:
                num2 = num2 % num1

        return num1 or num2
