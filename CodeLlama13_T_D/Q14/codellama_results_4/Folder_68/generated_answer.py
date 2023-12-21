
def find_second_smallest_num(my_list):
    my_list = sorted(my_list)
    return my_list[1] if len(my_list) > 1 else None
