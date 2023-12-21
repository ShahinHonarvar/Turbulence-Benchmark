
def all_pos_ints_exclusive(lst):
    positive_ints = []
    for i in range(598, 767):
        if lst[i] > 0:
            positive_ints.append(lst[i])
    return positive_ints
