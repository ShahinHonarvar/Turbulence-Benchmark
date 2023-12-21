
def all_pos_ints_inclusive(my_list):
    pos_ints = []
    for i in range(100, 201):
        if my_list[i - 100] > 0:
            pos_ints.append(my_list[i - 100])
    return pos_ints
