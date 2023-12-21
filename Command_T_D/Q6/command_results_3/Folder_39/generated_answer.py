def all_neg_ints_exclusive(lst):
    negative = lst[43:99]
    if not negative:
        return []
    return [i for i in negative if i < 0]
