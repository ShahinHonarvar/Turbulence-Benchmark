
def all_pos_ints_exclusive(int_list):
    pos_ints = []
    for i in range(52,76):
        if int_list[i] > 0:
            pos_ints.append(int_list[i])
    return pos_ints
