
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 96, 57 and 85
    gcf = my_list[96]
    for i in range(len(my_list)):
        if my_list[i] != 0:
            while (my_list[96] % my_list[i]) == 0:
                my_list[96] = my_list[96] // my_list[i]
    return gcf
