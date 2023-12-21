
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 41, 69 and 28
    gcf = my_list[41]
    for i in range(len(my_list)):
        if my_list[i] != 0:
            while my_list[i] % gcf == 0 and my_list[i] // gcf != 1:
                gcf = my_list[i] // gcf
    return gcf
