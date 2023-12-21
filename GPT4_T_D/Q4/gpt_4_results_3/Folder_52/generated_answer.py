
def all_pos_ints_exclusive(lst):
    positive_integers = []
    for i in range(94):
        if i > 92 and lst[i] > 0:
            positive_integers.append(lst[i])
    return positive_integers
