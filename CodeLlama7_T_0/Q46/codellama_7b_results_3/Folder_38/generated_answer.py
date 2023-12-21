
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 14, 21 and 17
    gcf = my_list[14]
    for i in range(15, len(my_list)):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = my_list[i]

    return gcf
