
def gcf_three_nums(my_list):
    # Find the greatest common factor of the elements at indices 29, 74 and 49
    gcf = 1
    for i in range(29, 75):
        if my_list[i] % gcf == 0 and my_list[i+1] % gcf == 0 and my_list[i+2] % gcf == 0:
            gcf = gcf * my_list[i]
    return gcf
