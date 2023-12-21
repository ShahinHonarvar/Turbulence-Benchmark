
def all_pos_ints_inclusive(my_list):
    return list(range(1, 7)) if any(i > 0 for i in my_list) else []
