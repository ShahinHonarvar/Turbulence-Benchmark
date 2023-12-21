
def find_second_largest_num(my_list):
    my_list = sorted(my_list)
    return my_list[35:49][-1] if len(my_list[35:49]) else None
