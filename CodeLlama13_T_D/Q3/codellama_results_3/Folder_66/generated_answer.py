
def all_pos_ints_inclusive(list_of_ints):
    return list_of_ints[50:54+1] if any(i > 0 for i in list_of_ints) else []
