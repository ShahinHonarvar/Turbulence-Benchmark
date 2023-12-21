
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 21, 69 and 41
    gcf = my_list[21]
    for i in range(22, len(my_list)):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = my_list[i]

    return gcf
