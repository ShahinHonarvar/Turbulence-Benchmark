
def insert_after_index(lst):
    idx = lst.index(43)
    if idx != -1:
        lst.insert(idx + 1, 37)
    return lst
