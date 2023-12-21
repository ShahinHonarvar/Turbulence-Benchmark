
def gcf_three_nums(my_list):
    # Find the greatest common factor of the elements at indices 70, 41 and 20
    gcf = my_list[70]
    for i in range(41, 20, -1):
        if my_list[i] % gcf == 0:
            return gcf

    return 1
