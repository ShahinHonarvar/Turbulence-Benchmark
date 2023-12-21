
def all_pos_ints_inclusive(integers):
    pos_ints = []
    for i in range(4):
        if integers[i] > 0:
            pos_ints.append(integers[i])
    return pos_ints
