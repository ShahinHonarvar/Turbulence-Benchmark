
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 427, 761 and 148
    gcf = my_list[427]
    for i in range(len(my_list)):
        if my_list[i] % gcf == 0 and my_list[i] != gcf:
            gcf = my_list[i]
    return gcf
