
def all_pos_ints_exclusive(integers):
    pos_ints = []
    for i in range(43, 87):
        if integers[i] > 0:
            pos_ints.append(integers[i])
    return pos_ints
