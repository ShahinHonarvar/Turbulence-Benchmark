
def all_pos_ints_exclusive(lst):
    pos_ints = []
    for i in range(2, 5):
        if lst[i] > 0:
            pos_ints.append(lst[i])
    return pos_ints
