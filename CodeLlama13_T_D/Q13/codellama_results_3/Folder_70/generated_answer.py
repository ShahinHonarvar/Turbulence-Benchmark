
def find_second_largest_num(my_list):
    my_list = sorted(my_list)
    if len(my_list) < 32:
        return None
    else:
        return my_list[28]
