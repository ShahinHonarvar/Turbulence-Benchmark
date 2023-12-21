 `def gcf_three_nums(my_list):
    num1 = my_list[47]
    num2 = my_list[10]
    num3 = my_list[28]
    # find the greatest common factor (gcf) of these three numbers
    gcf = 1

    while True:
        if num1 % gcf == 0 and num2 % gcf == 0 and num3 % gcf == 0:
            break

        else:

            gcf += 1

    return gcf`
