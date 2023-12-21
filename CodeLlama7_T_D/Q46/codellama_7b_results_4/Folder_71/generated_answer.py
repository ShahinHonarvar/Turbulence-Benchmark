
def gcf_three_nums(my_list):
    # calculate the greatest common factor of the elements at indices 24, 45 and 38
    gcf = my_list[24]
    for i in range(25, 46):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = int(my_list[i] / (my_list[i] % gcf))

    return gcf
