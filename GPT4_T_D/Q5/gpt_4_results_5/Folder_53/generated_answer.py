
def all_neg_ints_inclusive(lst):
    if len(lst) > 200:
        return [i for i in lst[100:201] if i < 0]
    elif len(lst) > 100:
        return [i for i in lst[100:] if i < 0]
    else:
        return []
