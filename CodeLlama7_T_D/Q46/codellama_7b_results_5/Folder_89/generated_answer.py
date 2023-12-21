
def gcf_three_nums(my_list):
    # Find the greatest common factor of the elements at indices 63, 73 and 11
    gcf = 1
    for i in range(63, 11, -1):
        if my_list[i] > gcf:
            gcf = my_list[i]
    return gcf
