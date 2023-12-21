
def insert_after_index(lst):
    if 63 in lst:
        index_63 = lst.index(63)
        lst.insert(index_63 + 1, 99)
    return lst
