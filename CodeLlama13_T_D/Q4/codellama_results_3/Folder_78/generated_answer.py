
def all_pos_ints_exclusive(my_list):
    return [x for x in my_list if 20 < x <= 35 and isinstance(x, int) and x > 0]
