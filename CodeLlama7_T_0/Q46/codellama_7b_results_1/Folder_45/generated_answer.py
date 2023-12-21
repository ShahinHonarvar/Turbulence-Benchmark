
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 46, 84 and 23
    gcf = my_list[46]
    for i in range(47, 85):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = my_list[i]

    return gcf
