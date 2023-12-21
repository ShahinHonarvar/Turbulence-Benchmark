
def gcf_three_nums(my_list):
    # Find the greatest common factor of the elements at indices 10, 55 and 36 in the list
    gcf = my_list[10]
    for i in range(10, 55):
        if my_list[i] % my_list[10] == 0:
            gcf = my_list[i]
    for i in range(36, len(my_list)):
        if my_list[i] % gcf == 0:
            return gcf
