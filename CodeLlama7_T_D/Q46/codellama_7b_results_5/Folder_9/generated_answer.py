
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 66, 90 and 27
    gcf = my_list[66]
    for i in range(len(my_list)):
        if my_list[i] != 1:
            while my_list[i] % gcf == 0:
                gcf = my_list[i]
    return gcf
