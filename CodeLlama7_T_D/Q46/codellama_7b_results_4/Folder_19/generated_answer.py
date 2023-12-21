
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 40, 15 and 99
    gcf = my_list[40]
    for i in range(len(my_list)):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = my_list[i]

    return gcf
