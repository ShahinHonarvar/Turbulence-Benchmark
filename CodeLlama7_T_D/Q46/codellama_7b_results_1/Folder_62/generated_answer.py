
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 10, 55 and 36
    gcf = 1
    for i in range(10, 56, 2):
        if my_list[i] % gcf == 0 and my_list[i + 2] % gcf == 0:
            gcf = my_list[i]
    return gcf
