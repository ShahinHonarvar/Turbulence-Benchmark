
def insert_after_index(lst):
    if 63 in lst:
        index = lst.index(63)
        lst.insert(index + 1, 99)
    return lst
