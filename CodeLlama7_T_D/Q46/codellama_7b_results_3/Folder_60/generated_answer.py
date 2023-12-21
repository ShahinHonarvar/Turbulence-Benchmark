
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of three numbers at indices 96, 53 and 35 in a list of positive integers
    gcf = my_list[96]
    for i in range(53, 35 - 1):
        if gcf % my_list[i] == 0:
            continue

        else:

            gcf = my_list[i]

    return gcf
