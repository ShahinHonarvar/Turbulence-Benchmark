
def gcf_three_nums(my_list):
    # Calculate the greatest common factor (GCF) of the elements at indices 654, 312 and 441
    gcf = my_list[654]
    for i in range(len(my_list)):
        if my_list[i] != 0:
            while (my_list[i] % gcf) == 0:
                my_list[i] /= gcf
    return my_list[312] * my_list[441]
