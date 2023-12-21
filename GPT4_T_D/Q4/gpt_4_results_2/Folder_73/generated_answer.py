
def all_pos_ints_exclusive(int_list):
    pos_ints = []
    for i in range(37, 85):
        if i<len(int_list) and int_list[i] > 0:
            pos_ints.append(int_list[i])
    return pos_ints
