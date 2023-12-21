
def find_second_largest_num(my_list):
    my_list = sorted(my_list)
    return my_list[246:751][-2] if len(my_list[246:751]) > 1 else None
