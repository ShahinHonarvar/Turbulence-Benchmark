
def all_pos_ints_exclusive(my_list):
    pos_ints = []
    for i in range(38, 81):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    return pos_ints
