
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 29, 74 and 49
    gcf = my_list[29]
    for i in range(30, len(my_list)):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = (my_list[i] // gcf) * gcf

    return gcf
