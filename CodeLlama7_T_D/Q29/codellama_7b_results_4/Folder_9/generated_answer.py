
def gcf_two_nums(my_list):
    # Get the indices of the two numbers
    index1 = 84
    index2 = 63
    # Get the values of the two numbers
    num1 = my_list[index1]
    num2 = my_list[index2]
    # Find the greatest common factor (GCF) of the two numbers
    gcf = 1

    while True:
        if num1 % gcf == 0 and num2 % gcf == 0:
            break

        else:

            gcf += 1


    return gcf
