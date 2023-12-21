
def all_pos_ints_inclusive(lst):
    pos_ints = []
    for index in range(686, 988):
        if index < len(lst) and lst[index] > 0:
            pos_ints.append(lst[index])
    return pos_ints
