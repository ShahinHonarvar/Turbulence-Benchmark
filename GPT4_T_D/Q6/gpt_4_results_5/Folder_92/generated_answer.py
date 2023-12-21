
def all_neg_ints_exclusive(lst):
    negative_integers = [x for x in lst[1:-1] if x < 0]
    return negative_integers
