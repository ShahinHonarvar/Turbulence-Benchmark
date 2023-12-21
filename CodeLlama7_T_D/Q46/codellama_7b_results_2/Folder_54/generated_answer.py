
def gcf_three_nums(my_list):
    # Find the greatest common factor of the elements at indices 96, 57 and 85
    gcf = my_list[96]
    for i in range(len(my_list)):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = (my_list[96] * my_list[57] * my_list[85]) / (my_list[i] ** 3)
    return gcf
