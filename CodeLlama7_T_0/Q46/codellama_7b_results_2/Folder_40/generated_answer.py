
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 1, 6 and 8
    gcf = my_list[1]
    for i in range(2, len(my_list)):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = my_list[i]

    return gcf
