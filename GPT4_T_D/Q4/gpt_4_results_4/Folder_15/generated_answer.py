
def all_pos_ints_exclusive(int_list):
    pos_int_list = []
    for i in range(1, 3):
        if int_list[i] > 0:
            pos_int_list.append(int_list[i])
    return pos_int_list
