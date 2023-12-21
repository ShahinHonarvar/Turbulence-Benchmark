
def find_second_largest_num(my_list):
    my_list = sorted(set(my_list))
    if len(my_list) < 4:
        return None
    else:
        return my_list[3]
