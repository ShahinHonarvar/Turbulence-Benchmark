
def all_pos_ints_inclusive(lst):
    positive_ints = []
    for i in range(56, 58):
        if i < len(lst):
            if lst[i] > 0:
                positive_ints.append(lst[i])
    return positive_ints
