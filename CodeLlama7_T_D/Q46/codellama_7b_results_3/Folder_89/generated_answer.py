
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 63, 73 and 11
    idx_63 = my_list[63]
    idx_73 = my_list[73]
    idx_11 = my_list[11]
    gcf = idx_63 * idx_73 * idx_11
    for i in range(2, int(gcf ** 0.5) + 1):
        if (idx_63 % i == 0) and (idx_73 % i == 0) and (idx_11 % i == 0)):
            gcf = i

    return gcf
