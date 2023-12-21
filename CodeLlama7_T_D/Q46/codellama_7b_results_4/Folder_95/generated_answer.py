
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 87, 20 and 36
    gcf = my_list[87]
    for i in range(20, 36 + 1):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = (my_list[i] // gcf) * gcf

    return gcf
