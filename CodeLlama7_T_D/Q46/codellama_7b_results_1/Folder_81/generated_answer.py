
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 20, 17 and 28
    gcf = my_list[20] * my_list[17] * my_list[28]
    for i in range(min(my_list[20], my_list[17], my_list[28]))):
        if (my_list[20] % i == 0) and (my_list[17] % i == 0) and (my_list[28] % i == 0)):
            gcf = i

    return gcf
