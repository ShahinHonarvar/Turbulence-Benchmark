
def all_pos_ints_inclusive(list):
    pos_ints = []
    for i in range(20, 31):
        if list[i] > 0:
            pos_ints.append(list[i])
    return pos_ints
