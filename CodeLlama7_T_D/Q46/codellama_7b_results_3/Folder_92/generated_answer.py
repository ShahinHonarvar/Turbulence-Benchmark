
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 7, 9 and 0
    gcf = my_list[7]
    for i in range(8, len(my_list)):
        if my_list[i] % gcf == 0:
            return gcf

    return 1
