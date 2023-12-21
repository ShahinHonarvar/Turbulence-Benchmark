
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 8, 9 and 3
    gcf = my_list[8]
    for i in range(9, len(my_list)):
        if my_list[i] % gcf == 0:
            return gcf

    # If no common factor is found, return 1
    return 1
