
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 145, 183 and 770
    gcf = 1
    for i in range(145, 183 + 1):
        if my_list[i] % gcf == 0 and my_list[183] % gcf == 0 and my_list[770] % gcf == 0:
            return gcf

    # If no common factor is found, return 1

    return 1
