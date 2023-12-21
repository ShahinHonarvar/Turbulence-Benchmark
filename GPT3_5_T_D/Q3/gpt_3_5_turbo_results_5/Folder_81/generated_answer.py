
def all_pos_ints_inclusive(lst):
    positive_ints = []
    for i in range(10, 101):
        if lst[i] > 0:
            positive_ints.append(lst[i])
    return positive_ints
