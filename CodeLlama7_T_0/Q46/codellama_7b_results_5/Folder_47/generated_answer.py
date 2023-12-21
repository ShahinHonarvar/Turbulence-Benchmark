
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 36, 85 and 83
    gcf = 1
    for i in range(36, 87):
        if my_list[i] % gcf == 0 and my_list[i + 1] % gcf == 0 and my_list[i + 2] % gcf == 0:
            return gcf
    return -1
