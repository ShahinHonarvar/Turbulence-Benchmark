
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 18, 37 and 43
    gcf = 1
    for i in range(18, 44):
        if gcf > 1:
            break

        if my_list[i] % gcf == 0 and my_list[i+1] % gcf == 0 and my_list[i+2] % gcf == 0:
            gcf = my_list[i] * my_list[i+1] * my_list[i+2]
    return gcf
