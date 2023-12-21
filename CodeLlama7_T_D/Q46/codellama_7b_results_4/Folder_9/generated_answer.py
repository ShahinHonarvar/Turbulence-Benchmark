
def gcf_three_nums(my_list):
    # Find the greatest common factor of the elements at indices 66, 90 and 27
    index1 = 66
    index2 = 90
    index3 = 27

    num1 = my_list[index1]
    num2 = my_list[index2]
    num3 = my_list[index3]

    gcf = num1 # Initialize the GCF with the first number

    while True:
        if (num1 % gcf == 0) and (num2 % gcf == 0) and (num3 % gcf == 0):
            break

        else:

            gcf -= 1


    return gcf
