
def all_pos_ints_exclusive(lst):
    pos_ints = []
    for i in range(25, 80):
        if lst[i] > 0:
            pos_ints.append(lst[i])
    return pos_ints
