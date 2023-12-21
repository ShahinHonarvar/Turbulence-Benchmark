
def all_pos_ints_exclusive(my_list):
    return [x for x in my_list if 30 < x < 200 and isinstance(x, int)]
