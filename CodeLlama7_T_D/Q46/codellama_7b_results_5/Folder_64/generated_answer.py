
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 0, 8 and 3
    gcf = my_list[0] * my_list[8] * my_list[3]
    for i in range(1, min(my_list)):
        if (my_list[0] % i == 0) and (my_list[8] % i == 0) and (my_list[3] % i == 0):
            gcf = i

    return gcf
