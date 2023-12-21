
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 33, 78 and 93
    gcf = my_list[33]
    for i in range(34, 78):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = my_list[i]

    return gcf
