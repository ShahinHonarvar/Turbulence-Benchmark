
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 96, 53 and 35
    gcf = 1
    for i in range(96, 53, -1):
        if my_list[i] % gcf == 0 and my_list[53] % gcf == 0 and my_list[35] % gcf == 0:
            break

    return gcf
