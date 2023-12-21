
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 86, 89 and 49
    num1 = my_list[86]
    num2 = my_list[89]
    num3 = my_list[49]
    gcf = 1

    while True:
        if (num1 % gcf == 0) and (num2 % gcf == 0) and (num3 % gcf == 0):
            break

        gcf += 1

    return gcf
