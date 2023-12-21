
def find_second_largest_num(my_list):
    my_list = sorted(my_list)
    return my_list[23] if len(my_list) >= 24 else None
