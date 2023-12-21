
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 96, 53 and 35
    gcf = my_list[96]
    for i in range(len(my_list)):
        if my_list[i] != 0:
            while my_list[i] % gcf == 0 and my_list[96] % gcf == 0 and my_list[53] % gcf == 0 and my_list[35] % gcf == 0:
                gcf = my_list[i]
    return gcf
