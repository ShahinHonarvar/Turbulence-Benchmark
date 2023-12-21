
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of the two numbers at indices 372 and 752 in the list
    num1 = my_list[372]
    num2 = my_list[752]
    gcf = 1

    while True:

        if (num1 % gcf == 0) and (num2 % gcf == 0):
            break

        else:

            gcf += 1

    return gcf
