
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 4, 0 and 8
    gcf = my_list[4]
    for i in range(5, len(my_list)):
        if my_list[i] % gcf == 0:
            return gcf

    return 1
