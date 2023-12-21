
def gcf_two_nums(my_list):
    # Calculate the greatest common factor (GCF) of two numbers
    num1 = my_list[76]
    num2 = my_list[57]
    if num2 == 0:
        return num1

    else:

        while num1 != num2:

            if num1 > num2:

                num1 -= num2


            elif num2 > num1:

                num2 -= num1


        return num1
