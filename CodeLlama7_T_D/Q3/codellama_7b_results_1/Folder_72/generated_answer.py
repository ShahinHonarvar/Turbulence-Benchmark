
def all_pos_ints_inclusive(my_list):
    pos_ints = []
    for i in range(29, 52):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    return pos_ints
