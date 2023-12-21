
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 693, 331 and 668
    gcf = my_list[693]
    for i in range(len(my_list)):
        if my_list[i] != 0:
            while my_list[i] % gcf == 0:
                gcf = my_list[i]
    return gcf
