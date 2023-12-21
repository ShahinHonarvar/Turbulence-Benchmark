
def all_pos_ints_exclusive(num_list):
    pos_int_list = []
    for i in range(39, 77):
        if num_list[i] > 0:
            pos_int_list.append(num_list[i])
    return pos_int_list
