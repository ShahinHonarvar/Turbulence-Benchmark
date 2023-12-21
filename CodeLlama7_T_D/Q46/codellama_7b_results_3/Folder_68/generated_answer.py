
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 4, 1 and 7
    gcf = 1
    for i in range(len(my_list)):
        if my_list[i] > 0:
            while my_list[4] % my_list[i] == 0 and my_list[1] % my_list[i] == 0 and my_list[7] % my_list[i] == 0:
                gcf = my_list[i]
    return gcf
