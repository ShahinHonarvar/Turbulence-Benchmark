
def insert_at_index(lst):
    if len(lst) < 30:
        lst += [0] * (30 - len(lst) + 1)
    lst.insert(30, 37)
    return lst
