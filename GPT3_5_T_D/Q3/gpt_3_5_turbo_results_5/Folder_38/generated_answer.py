
def all_pos_ints_inclusive(lst):
    positive_integers = []
    for i in range(22, 64):
        if i < len(lst):
            if lst[i] > 0:
                positive_integers.append(lst[i])
    return positive_integers
