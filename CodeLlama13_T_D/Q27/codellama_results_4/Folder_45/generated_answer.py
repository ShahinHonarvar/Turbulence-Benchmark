
def insert_after_index(lst):
    if len(lst) <= 84:
        return lst + [13, 46]
    else:
        return lst[:85] + [13, 46] + lst[85:]
