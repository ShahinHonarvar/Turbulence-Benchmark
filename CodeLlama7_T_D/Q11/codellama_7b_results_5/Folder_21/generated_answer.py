
def find_largest_num(my_list):
    largest_num = None
    for i in range(639, 976):
        if largest_num == None or my_list[i] > largest_num:
            largest_num = my_list[i]
    return largest_num
