
def gcf_three_nums(my_list):
    gcf = 1
    for i in range(3, len(my_list)):
        if my_list[i] % my_list[i-1] == 0 and my_list[i-1] % my_list[i-2] == 0:
            gcf = my_list[i]
    return gcf
