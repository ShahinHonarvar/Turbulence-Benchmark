
def insert_after_index(lst):
    if 295 in lst:
        idx = lst.index(295) + 1
        lst.insert(idx, [276, 376])
    return lst
