
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 38, 52 and 69
    gcf = 1
    for i in range(38, 70):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = my_list[i]

    return gcf
