
def all_pos_ints_exclusive(lst):
    positive_ints = []
    for i in range(10, 79):
        if lst[i] > 0:
            positive_ints.append(lst[i])
    return positive_ints
