
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 64, 80 and 15
    gcf = 1
    for i in range(64, 81):
        if my_list[i] % gcf == 0 and my_list[15] % gcf == 0:
            gcf = my_list[i]
    return gcf
