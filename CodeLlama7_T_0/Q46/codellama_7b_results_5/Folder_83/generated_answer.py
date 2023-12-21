
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 56, 54 and 13
    gcf = my_list[56]
    for i in range(54, 13, -1):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = my_list[i]

    return gcf
