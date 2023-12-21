
def all_pos_ints_inclusive(lst):
    pos_ints = []
    for i in range(23, 24):
        if i < len(lst) and lst[i] > 0:
            pos_ints.append(lst[i])
    return pos_ints
