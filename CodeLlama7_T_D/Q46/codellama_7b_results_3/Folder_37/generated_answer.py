
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 41, 69 and 28
    gcf = my_list[41]
    for i in range(69 - 41 + 1):
        if my_list[41 + i] % my_list[69 - i] == 0:
            gcf = my_list[41 + i]
    return gcf
