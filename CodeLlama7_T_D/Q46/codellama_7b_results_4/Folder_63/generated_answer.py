
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 38, 52 and 69
    gcf = 1
    for i in range(38, 69 + 1):
        if gcf == 1:
            gcf = my_list[i]
        else:
            while (my_list[i] % gcf) == 0:
                my_list[i] //= gcf
    return gcf
