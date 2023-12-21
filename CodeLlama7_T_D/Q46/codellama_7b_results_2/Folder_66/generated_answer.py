
def gcf_three_nums(my_list):
    # Calculate the greatest common factor (gcf) of three numbers
    num1 = my_list[92]
    num2 = my_list[69]
    num3 = my_list[95]
    gcf = 1

    while True:

        if num1 % gcf == 0 and num2 % gcf == 0 and num3 % gcf == 0:
            break

        else:

            gcf += 1


    return gcf
