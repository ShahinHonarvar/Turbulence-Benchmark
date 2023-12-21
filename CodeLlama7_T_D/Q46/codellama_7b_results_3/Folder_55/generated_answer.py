
def gcf_three_nums(my_list):
    # Get the greatest common factor of the elements at indices 9, 6 and 2
    gcf = my_list[9] * my_list[6] * my_list[2]
    for i in range(1, min(my_list[9], my_list[6], my_list[2])) + 1):
        if my_list[9] % i == 0 and my_list[6] % i == 0 and my_list[2] % i == 0:
            gcf = i
    return gcf
