
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 17, 88 and 35
    gcf = my_list[17]
    for i in range(17 + 1, len(my_list)):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = my_list[i]

    return gcf
