
def insert_after_index(lst):
    if 99 in lst:
        index99 = lst.index(99)
        lst.insert(index99+1, 99)
    return lst
