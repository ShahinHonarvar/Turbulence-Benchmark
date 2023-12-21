
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 33, 78 and 93
    gcf = 1
    for i in range(33, 78):
        if my_list[i] > 0:
            while (my_list[33] * my_list[78]) % my_list[93] == 0:
                gcf = my_list[33] * my_list[78]
    return gcf
