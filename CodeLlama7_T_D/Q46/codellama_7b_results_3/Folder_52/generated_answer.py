
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 19, 49 and 74
    gcf = my_list[19]
    for i in range(20, len(my_list)):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = my_list[i]

    return gcf
