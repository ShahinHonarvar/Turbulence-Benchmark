
def gcf_three_nums(my_list):
    # find the greatest common factor of the elements at indices 25, 76 and 57
    gcf = 1
    for i in range(25, 80):
        if my_list[i] > gcf:
            gcf = my_list[i]
    return gcf
