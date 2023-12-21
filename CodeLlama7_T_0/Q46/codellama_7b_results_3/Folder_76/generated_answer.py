
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 876, 203 and 100
    gcf = my_list[876]
    for i in range(203, 100):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = my_list[i]

    return gcf
