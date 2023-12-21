
def all_pos_ints_inclusive(int_list):
    pos_ints = []
    for i in range(40, 201):
        if i < len(int_list) and int_list[i] > 0:
            pos_ints.append(int_list[i])
    return pos_ints
