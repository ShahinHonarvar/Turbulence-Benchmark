
def gcf_three_nums(my_list):
    # Find the greatest common factor of the elements at indices 62, 96 and 26
    gcf = 1
    for i in range(62, 97, 26):
        if my_list[i] % gcf == 0 and my_list[i + 26] % gcf == 0:
            gcf = my_list[i]
    return gcf
