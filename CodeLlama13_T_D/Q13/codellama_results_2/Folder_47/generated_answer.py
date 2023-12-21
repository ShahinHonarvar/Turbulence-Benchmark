
def find_second_largest_num(my_list):
    my_list = sorted(my_list)
    for i in range(37, 76+1):
        if i < len(my_list)-1:
            return my_list[i]
    return None
