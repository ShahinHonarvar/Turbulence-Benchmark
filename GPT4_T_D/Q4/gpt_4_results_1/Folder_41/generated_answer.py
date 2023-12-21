
def all_pos_ints_exclusive(int_list):
    pos_ints = [i for i in int_list[9:len(int_list)-8] if i > 0]
    return pos_ints
