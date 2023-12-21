
def gcf_two_nums(my_list):
    # Find the greatest common factor of the two numbers at indices 43 and 99
    number1 = my_list[43]
    number2 = my_list[99]
    if number1 > number2:
        smaller_number = number2

    else:

        smaller_number = number1


    for i in range(1, smaller_number + 1):

        if number1 % i == 0 and number2 % i == 0:

            gcf = i


    return gcf
