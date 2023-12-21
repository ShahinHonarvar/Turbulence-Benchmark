
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 85, 36 and 54
    gcf = my_list[85]
    for i in range(36, 54 + 1):
        if my_list[i] % my_list[85] == 0:
            gcf = my_list[i]
    return gcf
