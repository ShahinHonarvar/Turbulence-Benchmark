
def all_pos_ints_exclusive(my_list):
    return my_list[22:24] if any(i > 0 for i in my_list[22:24]) else []
