
def insert_after_index(lst):
    if 295 in lst:
        index = lst.index(295)
        lst.insert(index + 1, [276, 376])
    return lst
