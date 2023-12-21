
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 24, 25 and 80
    gcf = my_list[24]
    for i in range(25, 80 + 1):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = my_list[i]

    return gcf
