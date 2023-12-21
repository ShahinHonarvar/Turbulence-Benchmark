
def all_pos_ints_inclusive(lst):
    pos_ints = []
    for i in range(686, 988):
        if 0 < i < len(lst) and lst[i] > 0:
            pos_ints.append(lst[i])
    return pos_ints
