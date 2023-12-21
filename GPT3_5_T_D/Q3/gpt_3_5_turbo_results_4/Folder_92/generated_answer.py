
def all_pos_ints_inclusive(lst):
    positive_integers = []
    for num in lst:
        if num >= 0:
            positive_integers.append(num)
    return positive_integers[:2]
