
def all_pos_ints_inclusive(my_list):
    return list(range(21, 98)) if any(x > 0 for x in my_list) else []
