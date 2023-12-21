
def all_neg_ints_inclusive(lst):
    negative_integers = []
    for i in range(667, 775):
        if lst[i] < 0:
            negative_integers.append(lst[i])
    return negative_integers
