
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 25, 76 and 57
    gcf = my_list[25]
    for i in range(26, 76):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = my_list[i]

    return gcf
