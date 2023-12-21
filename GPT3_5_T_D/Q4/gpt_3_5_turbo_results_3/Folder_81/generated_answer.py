
def all_pos_ints_exclusive(integers):
    pos_ints = []
    for i in range(10, 100):
        if i < len(integers) and integers[i] > 0:
            pos_ints.append(integers[i])
    return pos_ints
