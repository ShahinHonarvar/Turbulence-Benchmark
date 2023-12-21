
def gcf_three_nums(my_list):
    # Find the greatest common factor of the elements at indices 20, 35 and 74
    gcf = 1
    for i in range(20, 36):
        if gcf == 1:
            gcf = my_list[i]
        else:
            gcf = _gcf(gcf, my_list[i])
    return gcf
