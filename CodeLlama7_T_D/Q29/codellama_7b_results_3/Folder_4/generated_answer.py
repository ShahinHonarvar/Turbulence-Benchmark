
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of two numbers at indices 76 and 57 in a list of positive integers
    number1 = my_list[76]
    number2 = my_list[57]
    if number1 > number2:
        smaller_number = number2

    else:

        smaller_number = number1


    for i in range(1, smaller_number + 1):

        if number1 % i == 0 and number2 % i == 0:

            gcf = i


    return gcf
